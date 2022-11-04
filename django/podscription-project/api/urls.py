from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from typing import List
from api.schema import PodcastIn, PodcastOut
from api.models import Podcast

api = NinjaAPI()


@api.get("/podcasts", response=List[PodcastOut])
def list_podcasts(request):
    query = Podcast.objects.all()
    return query

@api.get("/podcasts/{podcast_id}", response=PodcastOut)
def get_podcast(request, podcast_id: int):
    return Podcast.objects.get(id=podcast_id)
    


urlpatterns = [
    path("", api.urls),
]
