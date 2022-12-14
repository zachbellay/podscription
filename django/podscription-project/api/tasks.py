import logging
import tempfile

import dateparser
import feedparser
import mutagen
import requests
import whisper
from api.models import Podcast, PodcastEpisode
from billiard import Process
from celery import shared_task
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask
from scrapers import settings as spider_settings
from scrapers.spiders.google_podcast import GooglePodcastSpider
from scrapy import signals
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from twisted.internet import asyncioreactor

from django.db import IntegrityError
from podscription.celery import app

from .utils import duration_to_seconds, group_text_by_time_window

model = None
model_size = "base"


logger = logging.getLogger(__name__)


class CeleryCrawlerProcess(Process):
    def __init__(self, spider, podcast_id: str):
        super().__init__()
        self.podcast_id = podcast_id
        # self.reactor = asyncioreactor.AsyncioSelectorReactor()
        self.crawler_settings = Settings()
        self.crawler_settings.setmodule(spider_settings)
        # self.crawler = CrawlerProcess(settings=self.crawler_settings)
        from scrapy.utils.log import configure_logging
        from scrapy.utils.project import get_project_settings

        settings = get_project_settings()
        # configure_logging({'LOG_LEVEL' : 'INFO'})

        self.crawler = CrawlerProcess({"LOG_LEVEL": "INFO"})
        # self.crawler = CrawlerRunner({'LOG_LEVEL' : 'INFO'})
        self.spider = spider

    def run(self):
        self.crawler.crawl(self.spider, podcast_id=self.podcast_id)
        self.crawler.start(stop_after_crawl=True, install_signal_handlers=True)


@app.task
def run_spider(podcast_id: str):

    spider = GooglePodcastSpider
    crawler = CeleryCrawlerProcess(spider, podcast_id=podcast_id)
    crawler.start()
    crawler.join()

    # send podcasts to transcription queue
    untranscribed_podcast_episodes = PodcastEpisode.objects.filter(
        podcast=podcast_id, transcription=None
    )
    for podcast_episode in untranscribed_podcast_episodes:
        transcribe_podcast_episode.delay(podcast_episode.id)


@app.task
def queue_untranscribed_podcast_episodes():
    eps = PodcastEpisode.objects.filter(transcription=None)
    for ep in eps:
        transcribe_podcast_episode.delay(ep.id)


@app.task
def queue_all_spiders():
    all_podcasts = Podcast.objects.all()

    for podcast in all_podcasts:
        run_spider.delay(podcast.id)


@app.task
def read_all_rss_feeds():
    all_podcasts = Podcast.objects.filter(is_rss=True)

    for podcast in all_podcasts:
        read_rss_feed.delay(podcast.id)


@app.task
def read_rss_feed(podcast_id: str):

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0"
    }

    podcast = Podcast.objects.get(id=podcast_id)

    if not podcast.is_rss:
        logger.warning("Podcast is not RSS: {podcast.name}")
        return

    feed = feedparser.parse(podcast.url)

    logger.info(f"Found {len(feed.entries)} episodes for {podcast.name}...")

    for entry in feed.entries:

        # Find the link to the audio file
        audio_url = None

        for link in entry.links:
            if link.type == "audio/mpeg":
                audio_url = link.href
                break

        if PodcastEpisode.objects.filter(audio_url=audio_url).exists():
            logger.info(f"Episode already exists: {podcast.name}-{entry.title}")
            continue

        duration = entry.itunes_duration
        duration = duration_to_seconds(duration)

        resolved_request = requests.head(
            audio_url, headers=headers, allow_redirects=True
        )

        logger.info(f"Resolved audio url: {resolved_request.url}")

        episode = PodcastEpisode(
            podcast=podcast,
            podcast_name=podcast.name,
            date=dateparser.parse(entry.published),
            title=entry.title,
            description=entry.description,
            audio_url=audio_url,
            resolved_audio_url=resolved_request.url,
            details_url=audio_url,
            duration=duration,
        )

        try:
            episode.save()
            logger.info(f"Added episode: {podcast.name}-{episode.title}")
        except IntegrityError:
            logger.info(f"Episode already exists: {podcast.name}-{episode.title}")
        except Exception as e:
            logger.error(f"Error saving episode: {podcast.name}-{episode.title}")
            logger.error(e)


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):

    print("Setting up periodic tasks...")
    
    # sender.add_periodic_task(
    #     3600 * 4, queue_untranscribed_podcast_episodes, name="Schedule transcription"
    # )

    sender.add_periodic_task(
        3600 * 4, read_all_rss_feeds, name="Schedule RSS feed reading"
    )


@app.task(queue="transcription_worker")
def transcribe_podcast_episode(podcast_episode_id: str):
    global model
    if not model:
        logger.info(f"Initializing whisper model of size {model_size}...")

        model = whisper.load_model(model_size)

    podcast_episode = PodcastEpisode.objects.get(id=podcast_episode_id)

    logger.info(
        f"Transcribing podcast episode\n id: {podcast_episode_id}\n title: {podcast_episode.title}\n podcast: {podcast_episode.podcast.name}\n date: {podcast_episode.date}\n"
    )

    if podcast_episode.whisper_transcription_object:
        logger.info("Podcast episode already has a transcription")
        return
    
    r = requests.get(podcast_episode.resolved_audio_url)

    audio_data = r.content

    logger.info(f"Audio data length: {len(audio_data)} bytes")

    f = tempfile.NamedTemporaryFile()
    f.write(audio_data)

    logger.info(f"Saved audio data to {f.name}")

    duration = int(mutagen.File(f.name).info.length)

    transcription_obj = model.transcribe(f.name, language="en", without_timestamps=True)

    transcription_full_text = transcription_obj["text"]
    grouped_transcription = group_text_by_time_window(
        transcription_obj, duration=duration
    )

    logger.info(f"Completed transcription")

    f.close()

    podcast_episode.transcription = grouped_transcription
    podcast_episode.transcription_full_text = transcription_full_text
    podcast_episode.duration = duration
    podcast_episode.whisper_transcription_object = transcription_obj
    podcast_episode.save()


@app.task(queue="transcription_worker")
def group_podcast_episode_transcript(podcast_episode_id: str):

    podcast_episode = PodcastEpisode.objects.get(id=podcast_episode_id)

    transcription_obj = podcast_episode.whisper_transcription_object

    transcription = group_text_by_time_window(
        transcription_obj, duration=podcast_episode.duration
    )

    podcast_episode.transcription = transcription

    podcast_episode.save()
