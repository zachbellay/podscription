# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from datetime import datetime

import dateparser
import scrapy
from scrapy_djangoitem import DjangoItem

from api.models import Podcast, PodcastEpisode

from urllib.parse import urljoin, urlparse

class PodcastItem(DjangoItem):
    django_model = Podcast


class PodcastEpisodeItem(DjangoItem):
    django_model = PodcastEpisode

    @staticmethod
    def parse_time(value):
        date = dateparser.parse(value)
        rounded = datetime(*date.timetuple()[:3])
        return rounded

    @staticmethod
    def parse_audio_url(value):
        start = value.find("http")
        end = value.find(";")
        return value[start:end] if end != -1 else value[start:]

    @staticmethod
    def parse_details_url(value):
        url = f"https://podcasts.google.com{value[1:]}"

        # remove query params
        url = urljoin(url, urlparse(url).path)
        return url



