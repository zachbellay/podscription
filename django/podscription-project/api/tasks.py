import logging
import tempfile

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

from podscription.celery import app

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


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):

    print("Setting up periodic tasks...")
    sender.add_periodic_task(
        3600 * 4, queue_all_spiders, name="Schedule spiders to scrape all podcasts"
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

    if podcast_episode.transcription:
        logger.info("Podcast episode already has a transcription")
        return

    r = requests.get(podcast_episode.audio_url)
    audio_data = r.content

    logger.info(f"Audio data length: {len(audio_data)} bytes")

    f = tempfile.NamedTemporaryFile()
    f.write(audio_data)

    logger.info(f"Saved audio data to {f.name}")

    transcription = model.transcribe(f.name, language="en", without_timestamps=True)
    transcription_text = transcription["text"]

    logger.info(f"Completed transcription")

    f.close()

    podcast_episode.transcription = transcription_text
    podcast_episode.save()
