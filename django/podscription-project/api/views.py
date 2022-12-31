from itertools import chain
from typing import Dict, List, Union

from api.models import Podcast, PodcastEpisode
from api.schema import (
    PodcastEpisodeLightOut,
    PodcastEpisodeOut,
    PodcastEpisodeSearchResultOut,
    PodcastOut,
)
from ninja import NinjaAPI
from ninja.errors import HttpError

# check if django debug is true
from django.conf import settings
from django.contrib import admin
from django.contrib.postgres.search import (
    SearchHeadline,
    SearchQuery,
    SearchRank,
    SearchVector,
    TrigramSimilarity,
)
from django.core.paginator import Paginator
from django.db.models import F, Value
from django.http import Http404
from django.shortcuts import get_object_or_404, render

if settings.DEBUG:
    api = NinjaAPI()
else:
    api = NinjaAPI(openapi_url=None)


@api.get(
    "/search/podcasts",
    response=List[PodcastOut],
    tags=["search"],
    operation_id="search_podcasts",
)
def search_podcasts(request, q: str):
    query = q

    podcast_by_name = (
        Podcast.objects.annotate(similarity=TrigramSimilarity("name", q))
        .filter(similarity__gt=0.3)
        .order_by("-similarity")
    )

    podcast_by_author = (
        Podcast.objects.annotate(similarity=TrigramSimilarity("author", q))
        .filter(similarity__gt=0.3)
        .order_by("-similarity")
    )

    #  combine the two queries and sort by similarity
    podcast_results = sorted(
        chain(podcast_by_name, podcast_by_author),
        key=lambda x: x.similarity,
        reverse=True,
    )

    podcast_results = list(set(podcast_results))[:3]

    return podcast_results


@api.get(
    "/search/episodes",
    response=List[PodcastEpisodeSearchResultOut],
    tags=["search"],
    operation_id="search_episodes",
)
def search_podcasts(request, q: str):
    query = q

    search_query = SearchQuery(query)
    search_headline = SearchHeadline(
        "transcription_full_text", search_query, min_words=40, max_words=60
    )

    podcast_episode_results = (
        PodcastEpisode.objects.annotate(headline=search_headline)
        .filter(search_vector=search_query, transcription__isnull=False)
        .order_by("-date")
    )[:10]

    return podcast_episode_results


@api.get(
    "/podcasts",
    response=List[PodcastOut],
    tags=["podcasts"],
    operation_id="list_podcasts",
)
def list_podcasts(request, page: int = 1):
    podcasts = Podcast.objects.filter(active=True)
    paginator = Paginator(podcasts, 20)
    page_obj = paginator.get_page(page)
    return page_obj.object_list


@api.get(
    "/podcasts/id/{podcast_id}",
    response=PodcastOut,
    tags=["podcasts"],
    operation_id="get_podcast",
)
def get_podcast(request, podcast_id: int):
    return get_object_or_404(Podcast, id=podcast_id, active=True)


@api.get(
    "/podcasts/slug/{podcast_slug}",
    response=PodcastOut,
    tags=["podcasts"],
    operation_id="get_podcast_by_slug",
)
def get_podcast_by_slug(request, podcast_slug: str):
    return get_object_or_404(Podcast, slug=podcast_slug, active=True)


@api.get(
    "/podcasts/{podcast_id}/episodes",
    response=List[PodcastEpisodeLightOut],
    tags=["podcast_episodes"],
    operation_id="list_podcast_episodes",
)
def list_podcast_episodes(request, podcast_id: int, page: int = 1):

    if not Podcast.objects.filter(id=podcast_id, active=True).exists():
        raise Http404("Podcast not found")

    podcast_episodes = (
        PodcastEpisode.objects.filter(podcast=podcast_id)
        .defer("transcription", "description", "audio_url", "details_url")
        .order_by("-date")
    )
    paginator = Paginator(podcast_episodes, 20)
    page_obj = paginator.get_page(page)
    return page_obj.object_list


@api.get(
    "/podcasts/{podcast_slug}/episodes/{episode_slug}",
    response=PodcastEpisodeOut,
    tags=["podcast_episodes"],
    operation_id="get_podcast_episode",
)
def get_podcast_episode(request, podcast_slug: str, episode_slug: str):
    return get_object_or_404(
        PodcastEpisode,
        slug=episode_slug,
        podcast__slug=podcast_slug,
        podcast__active=True,
    )
