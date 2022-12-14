# Generated by Django 4.1.3 on 2022-12-05 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Podcast",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("url", models.CharField(max_length=2048, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="PodcastEpisode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("audio_url", models.CharField(max_length=2048)),
                ("details_url", models.CharField(max_length=2048)),
                (
                    "transcription",
                    models.TextField(blank=True, default=None, null=True),
                ),
                (
                    "podcast",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.podcast"
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="podcast",
            constraint=models.UniqueConstraint(
                fields=("url",), name="unique_podcast_url"
            ),
        ),
        migrations.AddConstraint(
            model_name="podcastepisode",
            constraint=models.UniqueConstraint(
                fields=("details_url",), name="unique_podcast_episode_details_url"
            ),
        ),
    ]
