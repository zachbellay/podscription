#!/usr/bin/env bash
set -e

# Run tests
cd ./django/podscription-project
# python manage.py migrate
# python manage.py collectstatic --clear --noinput

echo "Starting celery whisper worker"

exec celery -A podscription worker -Q transcription_worker --loglevel=info -n transcription_worker --concurrency=2

#  --uid=nobody --gid=nogroup