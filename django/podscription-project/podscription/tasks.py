from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
from billiard import Process
from scrapy.utils.project import get_project_settings
from scrapy import signals
from celery import shared_task
from .celery import app
from celery.schedules import crontab
from scrapy.settings import Settings
from scrapers import settings as spider_settings
from django_celery_beat.models import PeriodicTask  

# from scrapers.spiders.the_daily_podcast import TheDailyPodcastSpider

from scrapers.spiders.example import ExampleSpider


@app.task
def ex(arg):
    print(arg)

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):

    PeriodicTask.objects.all().delete()

    print("setup_periodic_tasks")
    # # sender.add_periodic_task(30.0, ex.s('hello world'), name='add every 2')

    sender.add_periodic_task(5, run_spider, name='run spider every 30 seconds')


# from scrapy.crawler import CrawlerProcess



class UrlCrawlerScript(Process):
    def __init__(self, spider):
        Process.__init__(self)
        # settings = get_project_settings()
        self.crawler_settings = Settings()
        self.crawler_settings.setmodule(spider_settings)
        self.crawler = CrawlerProcess(settings=self.crawler_settings)
        
        # self.crawler.configure()
        # self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)

        # for crawler in self.crawlers:
        #     crawler.signals.connect(spider_ended, signal=scrapy.signals.spider_closed)


        self.spider = spider

    def run(self):
        # print('doing literally jack shit')
        self.crawler.crawl(self.spider)

        # print('========================================')
        # print(self.crawler_settings.copy_to_dict())
        # print('========================================')
        #     print('ayy lmao')

        # print(self.crawler_settings)
        self.crawler.start(stop_after_crawl=True, install_signal_handlers=True)
        # reactor.run()

@app.task
def run_spider():
    # spider = TheDailyPodcastSpider()
    spider = ExampleSpider
    crawler = UrlCrawlerScript(spider)
    crawler.start()
    crawler.join()

    print('hey sexy')