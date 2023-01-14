import requests
from bs4 import BeautifulSoup
from rangefilter.filters import DateRangeFilter

from django.contrib import admin

from .models import Podcast, PodcastEpisode
from .tasks import (
    group_podcast_episode_transcript,
    read_rss_feed,
    transcribe_podcast_episode,
)


@admin.action(description="Read RSS feed for selected podcasts")
def read_selected_rss_feeds(modeladmin, request, queryset):
    for podcast in queryset:
        read_rss_feed.delay(podcast.id)

    # read_rss_feeds.delay(list(queryset))


@admin.action(description="Re-run transcription on selected episodes")
def retranscribe_selected(modeladmin, request, queryset):
    for episode in queryset:
        episode.clear_transcriptions()
        transcribe_podcast_episode.delay(episode.id)


@admin.action(description="Re-run transcription grouping on selected episodes")
def rerun_transcription_grouping(modeladmin, request, queryset):
    for episode in queryset:
        episode.transcription = None
        episode.save()
        group_podcast_episode_transcript.delay(episode.id)



@admin.action(description="Update podcast information")
def update_select_podcasts(modeladmin, request, queryset):
    for podcast in queryset:

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0"
        }

        page = requests.get(podcast.url, headers=headers)

        soup = BeautifulSoup(page.content, "html.parser")

        title = soup.find(class_="ZfMIwb").get_text()
        author = soup.find(class_="BpVHBf").get_text()
        podcast_image = soup.find(class_="BhVIWc").get("src")
        description = soup.find(class_="OTAikb").get_text()
        website_url = soup.find(class_="jcGgqc").get("href")

        print(f"{title} by {author}")
        print(f"Description: {description}")
        print(f"Image: {podcast_image}")
        print(f"Website: {website_url}")

        success = Podcast.objects.filter(url=podcast.url).update(
            **{
                "name": title,
                "author": author,
                "url": podcast.url,
                "logo_url": podcast_image,
                "description": description,
                "website_url": website_url,
            }
        )

        if success:
            print("Successfully updated podcast")
        else:
            print("Failed to update podcast")


class PodcastAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "url")
    actions = [
        update_select_podcasts,
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
        rerun_transcription_grouping,
    ]

    search_fields = ("title", "podcast__name", "podcast__author")

    list_filter = (
        ("date", DateRangeFilter),
        ("transcription", admin.EmptyFieldListFilter),
    )


admin.site.register(Podcast, PodcastAdmin)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)
