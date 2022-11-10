import re

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
# from scrapers.items import (PodcastEpisodeItem, PodcastItem,
#                             PodcastTranscriptionItem)
from scrapers.items import (PodcastEpisodeItem, PodcastItem)
from scrapy.loader import ItemLoader
from scrapy_playwright.page import PageMethod
import tempfile

class TheDailyPodcastSpider(scrapy.Spider):
    name = "the-daily-podcast"
    temp_dir = tempfile.TemporaryDirectory()

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

    async def parse(self, response):

        url = response.url

        podcasts_div = response.css("div[role=list]")
        podcasts = podcasts_div.css("a[role=listitem]")

        podcast_episode_item = PodcastEpisodeItem()
        for podcast in podcasts:

            time, title, description = tuple(
                s.extract() for s in podcast.css("div[role=presentation]::text")
            )
            audio_url = podcast.css("div[jsdata]::attr(jsdata)").get()
            details_url = podcast.css("a::attr(href)").get()

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

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
    
    def close_spider(self, spider):
        self.temp_dir.cleanup()
