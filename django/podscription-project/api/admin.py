from django.contrib import admin
from .models import PodcastEpisode, Podcast
# Register your models here.

admin.site.register(Podcast)
admin.site.register(PodcastEpisode)

