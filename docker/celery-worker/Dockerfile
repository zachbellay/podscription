FROM python:3.10.1

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gcc
RUN apt-get install -y g++
RUN apt-get install -y build-essential
RUN apt-get install -y wget

USER root
RUN useradd -ms /bin/bash celery
RUN usermod -a -G celery celery
RUN usermod -a -G celery root

WORKDIR /usr/src/app
ADD ./docker/celery-worker/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt
RUN pip install watchdog

RUN playwright install-deps
RUN playwright install chromium

ADD ./docker ./docker

COPY ./docker/celery/celeryd /etc/init.d/
COPY ./docker/celery/celerybeat /etc/init.d/
COPY ./docker/celery/config/celeryd /etc/default/

RUN chmod 755 /etc/init.d/celeryd && \
    chmod 755 /etc/init.d/celerybeat && \
    chmod 640 /etc/default/celeryd && \
    chmod +x ./docker/celery-worker/entry.sh

ADD ./django ./django

ENTRYPOINT ["./docker/celery-worker/entry.sh"]
