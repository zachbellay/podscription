#!/usr/bin/env bash
set -e

cd ./django/podscription-project

echo "Starting celery whisper worker"

exec watchmedo auto-restart -d . -p '*.py' --recursive -- celery -A podscription worker -Q transcription_worker --loglevel=info -n transcription_worker --concurrency=2
