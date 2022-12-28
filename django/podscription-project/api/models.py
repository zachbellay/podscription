from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

# Create your models here.


class Podcast(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=2048, null=False, blank=False, unique=True)
    logo_url = models.CharField(max_length=2048, null=False, blank=False)
    description = models.TextField(null=False)
    website_url = models.CharField(max_length=2048, null=False, blank=False)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)
    is_rss = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["url"], name="unique_podcast_url")
        ]
        indexes = [
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return f"{self.name} by {self.author}"


class WhisperModelSize(models.TextChoices):
    TINY = "tiny", "tiny"
    BASE = "base", "base"
    SMALL = "small", "small"
    MEDIUM = "medium", "medium"
    LARGE = "large", "large"

class PodcastEpisode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    podcast_name = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateTimeField(null=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    audio_url = models.CharField(max_length=2048, null=False, blank=False)
    resolved_audio_url = models.CharField(max_length=2048, null=False, blank=False)
    details_url = models.CharField(max_length=2048, null=False, blank=False)
    transcription = models.JSONField(default=None, null=True, blank=True)
    transcription_full_text = models.TextField(blank=True, default=None, null=True)
    whisper_model_size = models.CharField(
        max_length=10,
        choices=WhisperModelSize.choices,
        default=WhisperModelSize.BASE,
    )
    whisper_transcription_object = models.JSONField(default=None, null=True, blank=True)
    duration = models.PositiveIntegerField(default=None, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    search_vector = SearchVectorField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["details_url"], name="unique_podcast_episode_details_url"
            )
        ]
        indexes = [
            GinIndex(fields=["search_vector"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return f"{self.podcast.name} - {self.title} - {self.date}"

    def clear_transcriptions(self):
        self.transcription = None
        self.whisper_transcription_object = None
        self.save()


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        if isinstance(instance, Podcast):
            instance.slug = unique_slug_generator(instance, "name")
        elif isinstance(instance, PodcastEpisode):
            instance.slug = unique_slug_generator(
                instance, "title", filter_args={"podcast": instance.podcast}
            )


pre_save.connect(pre_save_receiver, sender=Podcast)
pre_save.connect(pre_save_receiver, sender=PodcastEpisode)
