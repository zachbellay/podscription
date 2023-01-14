#!/usr/bin/env bash
set -e

cd ./django/podscription-project

echo "Starting celery worker"

exec celery -A podscription worker --beat -Q celery --loglevel=info --concurrency=4 --scheduler django_celery_beat.schedulers:DatabaseScheduler -n scraper_worker
