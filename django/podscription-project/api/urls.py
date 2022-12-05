from typing import List

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from api.models import Podcast, PodcastEpisode
from api.schema import PodcastEpisodeOut, PodcastOut



api = NinjaAPI()


@api.get("/podcasts", response=List[PodcastOut])
def list_podcasts(request):
    query = Podcast.objects.all()
    return query


@api.get("/podcasts/{podcast_id}", response=PodcastOut)
def get_podcast(request, podcast_id: int):
    return Podcast.objects.get(id=podcast_id)


@api.get("/podcasts/{podcast_id}/episodes", response=List[PodcastEpisodeOut])
def list_podcast_episodes(request, podcast_id: int):
    return PodcastEpisode.objects.filter(podcast=podcast_id)


@api.get("/podcasts/{podcast_id}/episodes/{episode_id}", response=PodcastEpisodeOut)
def get_podcast_episode(request, podcast_id: int, episode_id: int):
    return PodcastEpisode.objects.filter(podcast=podcast_id, id=episode_id)


urlpatterns = [
    path("", api.urls),
]
