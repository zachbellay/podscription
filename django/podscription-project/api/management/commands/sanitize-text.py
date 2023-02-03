from api.models import Podcast, PodcastEpisode
from api.utils import clean_description

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Sanitizes all podcast and podcast episode descriptions"

    def handle(self, *args, **kwargs):

        self.stdout.write('Sanitizing podcast descriptions...')

        for podcast in Podcast.objects.all():
            podcast.description = clean_description(podcast.description)
            podcast.save()

        self.stdout.write('Sanitizing podcast episode descriptions...')

        for podcast_episode in PodcastEpisode.objects.all():
            podcast_episode.description = clean_description(podcast_episode.description)
            podcast_episode.save()

        self.stdout.write(self.style.SUCCESS("Successfully sanitized descriptions"))
