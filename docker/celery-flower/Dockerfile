FROM python:3.10.1
EXPOSE 5555

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
# ADD ./requirements.txt ./requirements.txt

# RUN pip install -r ./requirements.txt

### temporary ###
# RUN pip install --upgrade pip setuptools
# ADD ./django/pyproject.toml ./
# ADD ./django/poetry.lock ./
# RUN pip install poetry
# RUN poetry config virtualenvs.create false

# RUN poetry install --only main --no-root
# RUN apt install postgresql-client -y
### this is to install django poetry dependencies, should be merged into one thing, but right now this is not the priority ###
### end temporary ###

ADD ./docker/celery-worker/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

ADD ./docker ./docker
ADD ./django ./django

COPY ./docker/celery/celeryd /etc/init.d/
COPY ./docker/celery/celerybeat /etc/init.d/
COPY ./docker/celery/config/celeryd /etc/default/
RUN ["chmod", "755", "/etc/init.d/celeryd"]
RUN ["chmod", "755", "/etc/init.d/celerybeat"]
RUN ["chmod", "640", "/etc/default/celeryd"]


RUN ["chmod", "+x", "./docker/celery-flower/entry.sh"]
ENTRYPOINT ["./docker/celery-flower/entry.sh"]
# ENTRYPOINT tail -f /dev/null
