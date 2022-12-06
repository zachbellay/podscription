from scrapy.crawler import CrawlerProcess, CrawlerRunner
from billiard import Process
from twisted.internet import asyncioreactor
from scrapy.utils.project import get_project_settings
from scrapy import signals
from celery import shared_task
from podscription.celery import app
from celery.schedules import crontab
from scrapy.settings import Settings
from scrapers import settings as spider_settings
from django_celery_beat.models import PeriodicTask  

from api.models import Podcast
from scrapers.spiders.google_podcast import GooglePodcastSpider

from podscription.celery import app
import whisper
import requests
from api.models import Podcast, PodcastEpisode
import tempfile

model = None
model_size = "base"

class CeleryCrawlerProcess(Process):
    def __init__(self, spider, podcast_id: str):
        super().__init__()
        self.podcast_id = podcast_id
        # self.reactor = asyncioreactor.AsyncioSelectorReactor()
        self.crawler_settings = Settings()
        self.crawler_settings.setmodule(spider_settings)
        self.crawler = CrawlerProcess(settings=self.crawler_settings)
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

    untranscribed_podcast_episodes = PodcastEpisode.objects.filter(podcast=podcast_id, transcription=None)
    for podcast_episode in untranscribed_podcast_episodes:
        transcribe_podcast_episode.delay(podcast_episode.id)

@app.task
def queue_all_spiders():
    all_podcasts = Podcast.objects.all()

    for podcast in all_podcasts:
        run_spider.delay(podcast.id)

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):

    print('Setting up periodic tasks...')
    sender.add_periodic_task(3600 * 4, queue_all_spiders, name='Schedule spiders to scrape all podcasts')

@app.task(queue='transcription_worker')
def transcribe_podcast_episode(podcast_episode_id: str):
    global model
    if not model:
        print(f'Initializing whisper model of size {model_size}...')
    
        model = whisper.load_model(model_size)

    podcast_episode = PodcastEpisode.objects.get(id=podcast_episode_id)

    if podcast_episode.transcription:
        raise ValueError("Podcast episode already has a transcription")
    
    r = requests.get(podcast_episode.audio_url)
    audio_data = r.content

    f = tempfile.NamedTemporaryFile()
    f.write(audio_data)

    transcription = model.transcribe(f.name, language="en", without_timestamps=True)
    transcription_text = transcription['text']

    f.close()

    podcast_episode.transcription = transcription_text
    podcast_episode.save()
