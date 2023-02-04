import logging

from api.models import Podcast, PodcastEpisode
from celery.schedules import crontab
from podscription.celery import app

logger = logging.getLogger(__name__)


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):

    print("Setting up periodic tasks...")

    sender.add_periodic_task(
        3600 * 4, queue_untranscribed_podcast_episodes, name="Schedule transcription"
    )

    sender.add_periodic_task(
        3600, read_all_rss_feeds, name="Schedule RSS feed reading"
    )


@app.task(queue="transcription_worker")
def queue_untranscribed_podcast_episodes():
    eps = PodcastEpisode.objects.filter(transcription=None)
    for ep in eps:
        app.send_task("api.task_worker.transcribe_podcast_episode", args=[ep.id])


@app.task(queue="rss_worker")
def read_all_rss_feeds():
    all_podcasts = Podcast.objects.filter(is_rss=True)

    for podcast in all_podcasts:
        app.send_task("api.task_worker.read_rss_feed", args=[podcast.id])
