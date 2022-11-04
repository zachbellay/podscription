from django.db import models

# Create your models here.

class Podcast(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=2048, null=False, blank=False)


class PodcastEpisode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)  
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    audio_url = models.CharField(max_length=2048, null=False, blank=False)
    details_url = models.CharField(max_length=2048, null=False, blank=False)
    transcibed = models.BooleanField(default=False)


class PodcastTranscription(models.Model):
    podcast_episode = models.ForeignKey(PodcastEpisode, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    