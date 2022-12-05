from django.contrib import admin

from .models import Podcast, PodcastEpisode
from .tasks import run_spider

# import api.tasks
# Register your models here.

@admin.action(description="Run spider on selected podcasts")
def run_spider_on_selected(modeladmin, request, queryset):
    for podcast in queryset:
        run_spider.delay(podcast.id)


class PodcastAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "url")
    actions = [run_spider_on_selected]

class PodcastEpisodeAdmin(admin.ModelAdmin):
    list_display = (
        "podcast",
        "date",
        "title",
    )
    

admin.site.register(Podcast, PodcastAdmin)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)
