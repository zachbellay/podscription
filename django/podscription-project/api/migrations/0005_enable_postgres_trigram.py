import django.contrib.postgres.indexes
from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_podcastepisode_api_podcast_search__18e659_gin'),
    ]

    operations = [
        TrigramExtension()
    ]
