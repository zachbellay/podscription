# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from api.models import Podcast, PodcastEpisode, PodcastTranscription
from scrapy_djangoitem import DjangoItem

class ScrapersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PodcastItem(DjangoItem):
    django_model = Podcast