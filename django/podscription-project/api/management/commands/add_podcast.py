import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand, CommandError
from api.models import Podcast

class Command(BaseCommand):
    help = 'Adds a podcast to the database'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='The URL of the podcast to add')
    
    def handle(self, *args, **kwargs):
        url = kwargs['url']

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0"
        }

        page = requests.get(url, headers=headers)

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

        podcast = Podcast(
            name=title,
            author=author,
            url=url,
            logo_url=podcast_image,
            description=description,
            website_url=website_url
        )
        podcast.save()

        self.stdout.write(self.style.SUCCESS('Successfully added podcast'))





