# Generated by Django 4.1.3 on 2022-12-18 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_podcast_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastepisode',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
