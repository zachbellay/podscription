from django.db import models

# Create your models here.


class Podcast(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=2048, null=False, blank=False, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["url"], name="unique_podcast_url")
        ]

    def __str__(self):
        return f"{self.name} by {self.author}"


class PodcastEpisode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    audio_url = models.CharField(max_length=2048, null=False, blank=False)
    details_url = models.CharField(max_length=2048, null=False, blank=False)
    transcription = models.TextField(default=None, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["details_url"], name="unique_podcast_episode_details_url"
            )
        ]

    def __str__(self):
        return f"{self.podcast.name} - {self.title} - {self.date}"
