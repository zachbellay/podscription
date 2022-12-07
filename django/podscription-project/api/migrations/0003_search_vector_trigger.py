from django.contrib.postgres.search import SearchVector
from django.db import migrations

def compute_search_vector(apps, schema_editor):
    PodcastEpisode = apps.get_model("api", "PodcastEpisode")
    PodcastEpisode.objects.update(search_vector=SearchVector('transcription', 'title', 'description', 'podcast_name'))

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_podcastepisode_podcast_name_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TRIGGER podcast_episode_search_vector_trigger
            BEFORE INSERT OR UPDATE OF transcription, title, description
            ON api_podcastepisode
            FOR EACH ROW EXECUTE PROCEDURE
            tsvector_update_trigger(
                search_vector, 'pg_catalog.english', transcription, title, description, podcast_name
            );
            UPDATE api_podcastepisode SET search_vector = NULL;
            """
        ),
        migrations.RunPython(compute_search_vector, reverse_code=migrations.RunPython.noop),
    ]