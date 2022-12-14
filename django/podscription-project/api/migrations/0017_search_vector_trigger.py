# Generated by Django 4.1.3 on 2022-12-28 07:22

from django.contrib.postgres.search import SearchVector
from django.db import migrations


def compute_search_vector(apps, schema_editor):
    PodcastEpisode = apps.get_model("api", "PodcastEpisode")
    PodcastEpisode.objects.update(
        search_vector=SearchVector("transcription_full_text", "title", "description")
    )


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0016_podcastepisode_transcription_full_text"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TRIGGER podcast_episode_search_vector_trigger
            BEFORE INSERT OR UPDATE OF transcription_full_text, title, description
            ON api_podcastepisode
            FOR EACH ROW EXECUTE PROCEDURE
            tsvector_update_trigger(
                search_vector, 'pg_catalog.english', transcription_full_text, title, description
            );
            UPDATE api_podcastepisode SET search_vector = NULL;
            """,
            reverse_sql="""
            DROP TRIGGER IF EXISTS podcast_episode_search_vector_trigger ON api_podcastepisode;
            """,
        ),
        migrations.RunPython(
            compute_search_vector, reverse_code=migrations.RunPython.noop
        ),
    ]
