import json
import random

import requests
from api.models import Podcast, PodcastEpisode
from api.utils import clean_description

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Abuses the castos API to search for a podcast's RSS feed from its name"

    def add_arguments(self, parser):
        parser.add_argument(
            "podcast-name", type=str, help="The name of the podcast"
        )

    def handle(self, *args, **kwargs):
        podcast_name = kwargs["podcast-name"]

        # generate 28 random numbers as a string
        # random_numbers = ''.join([str(random.randint(0, 9)) for i in range(28)])
        random_numbers='129673560618904815724195451105'


        # body = f"""-----------------------------{random_numbers}
        #     Content-Disposition: form-data; name="search"

        #     {podcast_name}
        #     -----------------------------{random_numbers}
        #     Content-Disposition: form-data; name="action"

        #     feed_url_lookup_search
        #     -----------------------------{random_numbers}--
        # """

        body=f"""-----------------------------{random_numbers}
Content-Disposition: form-data; name="search"

{podcast_name}
-----------------------------{random_numbers}
Content-Disposition: form-data; name="action"

feed_url_lookup_search
-----------------------------{random_numbers}--
"""

        headers = {
            'Host':'castos.com',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept':'*/*',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'gzip, deflate, br',
            'Referer':'https://castos.com/tools/find-podcast-rss-feed/',
            'Content-Type':f'multipart/form-data; boundary=---------------------------{random_numbers}',
            'Content-Length':f'{len(body)}',
            'Origin':'https://castos.com',
            'DNT':'1',
            'Connection':'keep-alive',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'Sec-GPC':'1',
            'Pragma':'no-cache',
            'Cache-Control':'no-cache',
            'TE':'trailers',
        }

        

        r = requests.post('https://castos.com/wp-admin/admin-ajax.php', headers=headers, data=body)


        # get status code and print it
        # if there is an error print the error


        response = r.content
        response = json.loads(response.decode('utf-8'))
        
        # check if the response is a success
        if response['success'] == True:
            # get the first element in the data field
            result = response['data'][0]
            title = result['title']
            author = result['author']
            rss_feed = result['url']
            
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"RSS Feed: {rss_feed}")
        



        # self.stdout.write('Sanitizing podcast descriptions...')

        # for podcast in Podcast.objects.all():
        #     podcast.description = clean_description(podcast.description)
        #     podcast.save()

        # self.stdout.write('Sanitizing podcast episode descriptions...')

        # for podcast_episode in PodcastEpisode.objects.all():
        #     podcast_episode.description = clean_description(podcast_episode.description)
        #     podcast_episode.save()

        # self.stdout.write(self.style.SUCCESS("Successfully sanitized descriptions"))
