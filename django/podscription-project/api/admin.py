import requests
from podscription.celery import app
from rangefilter.filters import DateRangeFilter

from django.contrib import admin

from .models import Podcast, PodcastEpisode
from .task_worker import transcribe_podcast_episode


@admin.action(description="Read RSS feed for selected podcasts")
def read_selected_rss_feeds(modeladmin, request, queryset):
    for podcast in queryset:
        # read_rss_feed.delay(podcast.id)
        app.send_task("api.task_worker.read_rss_feed", args=[podcast.id])
        

@admin.action(description="Re-run transcription on selected episodes")
def retranscribe_selected(modeladmin, request, queryset):
    for episode in queryset:
        episode.clear_transcriptions()
        # transcribe_podcast_episode.delay(episode.id)
        app.send_task("api.task_worker.transcribe_podcast_episode", args=[episode.id], queue='transcription_worker')


class PodcastAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "url")
    actions = [
        read_selected_rss_feeds,
    ]


class PodcastEpisodeAdmin(admin.ModelAdmin):
    list_display = (
        "podcast",
        "date",
        "title",
    )

    ordering = ("-date",)

    actions = [
        retranscribe_selected,
    ]

    search_fields = ("title", "podcast__name", "podcast__author")

    list_filter = (
        ("date", DateRangeFilter),
        ("transcription", admin.EmptyFieldListFilter),
    )

admin.site.register(Podcast, PodcastAdmin)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)
