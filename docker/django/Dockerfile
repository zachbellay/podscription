FROM python:3.10 as base

SHELL ["/bin/bash", "-c"] 

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y gcc g++ build-essential wget

WORKDIR /usr/src/app
RUN mkdir logs && touch ./logs/debug.log

RUN pip install --upgrade pip setuptools
RUN pip install poetry
RUN poetry config virtualenvs.create false

ADD ./django/pyproject.toml ./
ADD ./django/poetry.lock ./

RUN poetry install --only main --no-root
# RUN apt install postgresql-client -y

ADD ./django ./django
ADD ./docker ./docker

FROM base as prod
EXPOSE 8888
RUN chmod +x ./docker/django/entry.sh

# ENTRYPOINT tail -f /dev/null
CMD ./docker/django/entry.sh
