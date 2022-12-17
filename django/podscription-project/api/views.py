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

from django.db.models import F, Value
from django.contrib.postgres.search import TrigramSimilarity, SearchVector

from django.db.models import F

api = NinjaAPI()




# def search(query):
#     query = SearchQuery(query)
#     podcast_search_vector = SearchVector('name', weight='A') + SearchVector('author', weight='B')
#     podcasts = (
#         Podcast.objects.annotate(search=podcast_search_vector)
#         .annotate(similarity=TrigramSimilarity('search', query))
#         .filter(similarity__gt=0.3).order_by('-similarity')
#     )
#     podcast_episode_search_vector = SearchVector('transcription', weight='A') + SearchVector('description', weight='B')
#     episodes = PodcastEpisode.objects.annotate(
#         search=podcast_episode_search_vector,
#         similarity=TrigramSimilarity('search', query)
#     ).filter(similarity__gt=0.3, transcription__isnull=False).order_by('-similarity')
#     return list(podcasts) + list(episodes)

@api.get("/search", response=List[PodcastSearchResultOut], tags=['search'], operation_id='search')
def search(request, q: str):
    query = q

    podcasts = list(
        Podcast.objects.annotate(similarity=TrigramSimilarity('name', q))
        .filter(similarity__gt=0.3)    
        .order_by('-similarity')
    )

    podcasts += list(
        Podcast.objects.annotate(similarity=TrigramSimilarity('author', q))
        .filter(similarity__gt=0.3)
        .order_by('-similarity')
    )

    for p in podcasts:
        print(p.similarity)
    

    # TODO: Look into how to handle the case where a transcript hasn't been generated
    # but there is a match in the description. Should I show the description?

    search_query = SearchQuery(query)
    search_headline = SearchHeadline(
        "transcription",
        search_query,
        start_sel="",
        stop_sel=""
    )

    podcast_search_results = (
        PodcastEpisode.objects.filter(search_vector=search_query, transcription__isnull=False)
        .annotate(headline=search_headline)
        .annotate(rank=SearchRank(SearchVector('transcription'), search_query))
        .order_by("-rank")
    )[:10]

    for p in podcast_search_results:
        print(p.rank)

# description_search_results = (
# PodcastEpisode.objects.annotate(
#     search_description=SearchVector('description'),
#     rank=SearchRank(SearchVector('description'), SearchQuery('elon musk'))
# ).annotate(headline=SearchHeadline('description', SearchQuery('elon musk'))).filter(rank__gt=0.1).order_by('-date').first().description

    # query to search podcasts by name
    # Podcast.objects.annotate(headline=SearchHeadline('name', 'the daily'))
    # Podcast.objects.annotate(rank=SearchRank(SearchVector('name'), SearchQuery('today explained')))

    # podcast_search_results = (
    #     PodcastEpisode.objects.filter(search_vector=search_query, transcription__isnull=False)
    #     .annotate(rank=SearchRank(SearchVector('transcription'), search_query))
    #     .order_by("-rank")
    # )[:10]

    # podcast_search_results = (
    #     PodcastEpisode.objects.annotate(headline=search_headline)
    #     .filter(search_vector=search_query, transcription__isnull=False)
    #     .order_by("-date")
    # )[:10]


    results = [
        PodcastSearchResultOut(
            episode_id=podcast_episode.id,
            podcast=podcast_episode.podcast,
            headline=podcast_episode.headline,
        )
        for podcast_episode in podcast_search_results
    ]

    return results


@api.get("/podcasts", response=List[PodcastOut], tags=['podcasts'], operation_id='list_podcasts')
def list_podcasts(request, page: int = 1):
    podcasts = Podcast.objects.all()
    paginator = Paginator(podcasts, 20)
    page_obj = paginator.get_page(page)
    return page_obj.object_list


@api.get("/podcasts/{podcast_id}", response=PodcastOut, tags=['podcasts'], operation_id='get_podcast')
def get_podcast(request, podcast_id: int):
    return Podcast.objects.get(id=podcast_id)


@api.get("/podcasts/{podcast_id}/episodes", response=List[PodcastEpisodeLightOut], tags=['podcast_episodes'], operation_id='list_podcast_episodes')
def list_podcast_episodes(request, podcast_id: int, page: int = 1):
    podcast_episodes = (
        PodcastEpisode.objects.filter(podcast=podcast_id)
        .defer('transcription', 'description', 'audio_url', 'details_url')
        .order_by("-date")
    )
    paginator = Paginator(podcast_episodes, 20)
    page_obj = paginator.get_page(page)
    return page_obj.object_list


@api.get("/podcasts/{podcast_id}/episodes/{episode_id}", response=PodcastEpisodeOut, tags=['podcast_episodes'], operation_id='get_podcast_episode')
def get_podcast_episode(request, podcast_id: int, episode_id: int):
    return PodcastEpisode.objects.filter(podcast=podcast_id, id=episode_id).get()
