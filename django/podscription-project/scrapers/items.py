# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from datetime import datetime

import dateparser
import scrapy
from api.models import Podcast, PodcastEpisode
from scrapy_djangoitem import DjangoItem


class PodcastItem(DjangoItem):
    django_model = Podcast


class PodcastEpisodeItem(DjangoItem):
    django_model = PodcastEpisode
    audio_data_path = scrapy.Field()

    @staticmethod
    def parse_time(value):
        date = dateparser.parse(value)
        rounded = datetime(*date.timetuple()[:3])
        return rounded

    @staticmethod
    def parse_audio_url(value):
        start = value.find("http")
        return value[start:]

    @staticmethod
    def parse_details_url(value):
        url = f"https://podcasts.google.com{value[1:]}"
        return url


# class PodcastTranscriptionItem(DjangoItem):
#     django_model = PodcastTranscription