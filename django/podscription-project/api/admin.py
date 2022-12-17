from django.contrib import admin
from rangefilter.filters import DateRangeFilter
import requests
from bs4 import BeautifulSoup

from .models import Podcast, PodcastEpisode
from .tasks import run_spider

# import api.tasks
# Register your models here.

@admin.action(description="Run spider on selected podcasts")
def run_spider_on_selected(modeladmin, request, queryset):
    for podcast in queryset:
        run_spider.delay(podcast.id)


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

        success = Podcast.objects.filter(url=podcast.url).update(**{
            'name':title,
            'author':author,
            'url': podcast.url,
            'logo_url':podcast_image,
            'description':description,
            'website_url':website_url    
            }
        )
        
        if success:
            print('Successfully updated podcast')
        else:
            print('Failed to update podcast')




class PodcastAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "url")
    actions = [run_spider_on_selected, update_select_podcasts]

class PodcastEpisodeAdmin(admin.ModelAdmin):
    list_display = (
        "podcast",
        "date",
        "title",
    )

    search_fields = ("title", "podcast__name", "podcast__author")

    list_filter = (('date', DateRangeFilter),)
    

admin.site.register(Podcast, PodcastAdmin)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)
