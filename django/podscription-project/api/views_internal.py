from itertools import chain
from typing import Dict, List, Union

from api.models import Podcast, PodcastEpisode
from api.schema import (
    PodcastEpisodeLightOut,
    PodcastEpisodeOut,
    PodcastEpisodeSearchResultOut,
    PodcastOut,
)
from ninja import NinjaAPI, Router
from ninja.errors import HttpError

# check if django debug is true
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
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

router = Router()


@router.get(
    "/podcasts",
)
@user_passes_test(lambda u: u.is_superuser, login_url='/admin/login/')
def search_podcasts(request):
    return {"hello": "world"}




