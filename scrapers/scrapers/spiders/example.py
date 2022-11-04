import scrapy
from scrapers.items import PodcastItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        return PodcastItem(name='The Daily', author='The New York Times', url='https://www.nytimes.com/column/the-daily')
