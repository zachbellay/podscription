from typing import List

from django.contrib import admin

from django.shortcuts import render

from ninja import NinjaAPI

from api.models import Podcast, PodcastEpisode
from api.schema import PodcastEpisodeOut, PodcastOut, PodcastSearchResultOut, PodcastEpisodeLightOut

from django.core.paginator import Paginator

from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from django.db.models import F

api = NinjaAPI()


@api.get("/search", response=List[PodcastSearchResultOut])
def search(request, q: str):
    query = q
    
    search_query = SearchQuery(query)
    search_headline = SearchHeadline(
        "transcription", search_query, start_sel="", stop_sel=""
    )

    podcast_search_results = (
        PodcastEpisode.objects.filter(search_vector=query)
        .annotate(headline=search_headline)
        .order_by("-date")
    )[:10]

    results = [
        PodcastSearchResultOut(
            episode_id=podcast_episode.id,
            podcast=podcast_episode.podcast,
            headline=podcast_episode.headline,
        )
        for podcast_episode in podcast_search_results
    ]

    return results


@api.get("/podcasts", response=List[PodcastOut])
def list_podcasts(request, page: int = 0):
    podcasts = Podcast.objects.all()
    paginator = Paginator(podcasts, 20)
    page_obj = paginator.get_page(page)
    return page_obj.object_list


@api.get("/podcasts/{podcast_id}", response=PodcastOut)
def get_podcast(request, podcast_id: int):
    return Podcast.objects.get(id=podcast_id)


@api.get("/podcasts/{podcast_id}/episodes", response=List[PodcastEpisodeLightOut])
def list_podcast_episodes(request, podcast_id: int, page: int = 0):
    podcast_episodes = (
        PodcastEpisode.objects.filter(podcast=podcast_id)
        .defer('transcription', 'description', 'audio_url', 'details_url')
        .order_by("-date")
    )
    paginator = Paginator(podcast_episodes, 20)
    page_obj = paginator.get_page(page)
    return page_obj.object_list


@api.get("/podcasts/{podcast_id}/episodes/{episode_id}", response=PodcastEpisodeOut)
def get_podcast_episode(request, podcast_id: int, episode_id: int):
    return PodcastEpisode.objects.filter(podcast=podcast_id, id=episode_id)
