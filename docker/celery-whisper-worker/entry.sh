#!/usr/bin/env bash
set -e

cd ./django/podscription-project

echo "Starting celery whisper worker"

exec celery -A podscription worker -Q transcription_worker --loglevel=info -n transcription_worker --concurrency=2
