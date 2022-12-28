import feedparser
from api.models import Podcast

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Adds a podcast to the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "rss_url", type=str, help="The RSS URL of the podcast to add"
        )

    def handle(self, *args, **kwargs):
        rss_url = kwargs["rss_url"]

        feed = feedparser.parse(rss_url)

        podcast = Podcast(
            name=feed.feed.title,
            author=feed.feed.author,
            url=rss_url,
            logo_url=feed.feed.image.href if "image" in feed.feed else "",
            description=feed.feed.description,
            website_url=feed.feed.link,
            is_rss=True,
        )
        podcast.save()

        self.stdout.write(self.style.SUCCESS("Successfully added podcast"))
