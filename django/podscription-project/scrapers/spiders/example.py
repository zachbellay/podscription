import scrapy
from scrapers.items import PodcastItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):

        for _ in range(100):
            print('this should be parsing the response')
            
        yield PodcastItem(name='The Daily', author='The New York Times', url='https://www.nytimes.com/column/the-daily')
