
import re

import scrapy
from scrapy_playwright.page import PageMethod

import dateparser
from datetime import datetime

from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class Podcast(scrapy.Item):
    time = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    audio_url = scrapy.Field()
    details_url = scrapy.Field()

    @staticmethod
    def parse_time(value):
        date = dateparser.parse(value)
        rounded = datetime(*date.timetuple()[:3])
        return rounded
    
    @staticmethod
    def parse_audio_url(value):
        start = value.find('http')
        return value[start:]   

    @staticmethod
    def parse_details_url(value):
        url = f"https://podcasts.google.com{value[1:]}"
        return url


class TheDailyPodcastSpider(scrapy.Spider):
    name = 'the-daily-podcast'
   

    def start_requests(self):
        url = 'https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS81NG5BR2NJbA'
        yield scrapy.Request(url, meta=dict(
            playwright=True,
            playwright_include_page=True,
            errback=self.errback,
        ))

    async def parse(self, response):

        url = response.url

        podcasts_div = response.css('div[role=list]')
        podcasts = podcasts_div.css('a[role=listitem]')
        
        podcast_item = Podcast()
        for podcast in podcasts:     
            
            time, title, description = tuple(s.extract() for s in podcast.css('div[role=presentation]::text'))
            
            podcast_item['time'] = Podcast.parse_time(time)
            podcast_item['title'] = title
            podcast_item['description'] = description
            podcast_item['audio_url'] = Podcast.parse_audio_url(podcast.css('div[jsdata]::attr(jsdata)').get())
            podcast_item['details_url'] = Podcast.parse_details_url(podcast.css('a::attr(href)').get())


            yield podcast_item
            # yield loader.load_item()

        # screenshot = await page.screenshot(path=f"{name(url)}.png", full_page=True)

        # with open(f'./imgs/{name(url)}.png', 'wb') as f:
        #     f.write(screenshot)

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()