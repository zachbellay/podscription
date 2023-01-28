#!/usr/bin/env bash
set -e

cd ./django/podscription-project

echo "Starting flower"
exec celery -A podscription flower --address=0.0.0.0 --port=5555