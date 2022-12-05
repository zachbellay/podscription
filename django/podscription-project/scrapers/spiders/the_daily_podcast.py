import re

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from api.models import Podcast
# from scrapers.items import (PodcastEpisodeItem, PodcastItem,
#                             PodcastTranscriptionItem)
from scrapers.items import (PodcastEpisodeItem, PodcastItem)
from scrapy.loader import ItemLoader
from scrapy_playwright.page import PageMethod
# import tempfile
from copy import deepcopy

class TheDailyPodcastSpider(scrapy.Spider):
    name = "the-daily-podcast"
    # temp_dir = tempfile.TemporaryDirectory()

    # podcast = Podcast.objects.filter(name='The Daily', author='The New York Times').first()

    podcast, created = Podcast.objects.get_or_create(name='The Daily', author='The New York Times', url='https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS81NG5BR2NJbA')
   

    def start_requests(self):
        url = "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS81NG5BR2NJbA"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                errback=self.errback,
            ),
        )

    def parse(self, response):

        url = response.url

        podcasts_div = response.css("div[role=list]")
        podcast_episodes = podcasts_div.css("a[role=listitem]")
        
        for podcast_episode in podcast_episodes:
            podcast_episode_item = PodcastEpisodeItem()

            time, title, description = tuple(
                s.extract() for s in podcast_episode.css("div[role=presentation]::text")
            )
            audio_url = podcast_episode.css("div[jsdata]::attr(jsdata)").get()
            details_url = podcast_episode.css("a::attr(href)").get()

            
            podcast_episode_item['podcast'] = self.podcast
            podcast_episode_item["date"] = PodcastEpisodeItem.parse_time(time)
            podcast_episode_item["title"] = title
            podcast_episode_item["description"] = description
            podcast_episode_item["audio_url"] = PodcastEpisodeItem.parse_audio_url(
                audio_url
            )
            podcast_episode_item["details_url"] = PodcastEpisodeItem.parse_details_url(
                details_url
            )

            yield podcast_episode_item

    def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        page.close()
    
    # def close_spider(self, spider):
    #     self.temp_dir.cleanup()



