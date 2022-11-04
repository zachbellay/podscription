#!/usr/bin/env bash
set -e

cd ./podscription-project/
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --clear --noinput

rm -rf /usr/src/app/logs/
mkdir /usr/src/app/logs/
touch /usr/src/app/logs/gunicorn.log
touch /usr/src/app/logs/access.log

# exec python manage.py runserver 0.0.0.0:8888
exec gunicorn podscription.wsgi:application -w 2 -b :8888 --reload --access-logfile - --error-logfile -