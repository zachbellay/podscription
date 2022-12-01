from django.contrib import admin
from .models import PodcastEpisode, Podcast
# Register your models here.

class PodcastAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'url')

class PodcastEpisodeAdmin(admin.ModelAdmin):
    list_display = ('podcast', 'date', 'title',)


admin.site.register(Podcast, PodcastAdmin)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)

