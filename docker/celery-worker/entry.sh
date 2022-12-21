#!/usr/bin/env bash
set -e

# Run tests
cd ./django/podscription-project
# python manage.py migrate
# python manage.py collectstatic --clear --noinput

echo "Starting celery worker"

exec watchmedo auto-restart -d . -p '**/**.py' -- celery -A podscription worker --beat -Q celery --loglevel=info --concurrency=4 --scheduler django_celery_beat.schedulers:DatabaseScheduler -n scraper_worker

#  --uid=nobody --gid=nogroup