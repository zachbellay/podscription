import re

from copy import deepcopy

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from scrapy_playwright.page import PageMethod

from api.models import Podcast

from scrapers.items import PodcastEpisodeItem, PodcastItem


class GooglePodcastSpider(scrapy.Spider):
    name = "google-podcast-spider"

    def __init__(self, podcast_id: str):
        self.podcast = Podcast.objects.filter(id=podcast_id).first()

    def start_requests(self):
        url = self.podcast.url
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

        for podcast_episode in reversed(podcast_episodes):
            podcast_episode_item = PodcastEpisodeItem()

            time, title, description = tuple(
                s.extract() for s in podcast_episode.css("div[role=presentation]::text")
            )
            audio_url = podcast_episode.css("div[jsdata]::attr(jsdata)").get()
            details_url = podcast_episode.css("a::attr(href)").get()

            podcast_episode_item["podcast"] = self.podcast
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
