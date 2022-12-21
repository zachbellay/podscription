#!/usr/bin/env bash
set -e

cd ./django/podscription-project
# python manage.py migrate
# python manage.py collectstatic --clear --noinput

echo "Starting flower"
exec celery -A podscription flower --address=0.0.0.0 --port=5555
