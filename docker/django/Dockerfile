FROM node:19 as builder

WORKDIR /usr/src/app

ADD package.json package-lock.json tsconfig.json tsconfig.node.json tailwind.config.cjs postcss.config.cjs vite.config.ts openapitools.json ./

RUN npm install

ADD ./django/podscription-project/static/src ./django/podscription-project/static/src
#ADD .env.production .env.production
#ADD .env.development .env.development

RUN npm run build

ENTRYPOINT tail -f /dev/null

# ================================

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

ADD ./docker/celery-worker/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

RUN pip install --upgrade pip setuptools
RUN pip install poetry
RUN poetry config virtualenvs.create false

ADD ./django/pyproject.toml ./
ADD ./django/poetry.lock ./


RUN poetry install --only main --no-root
# RUN apt install postgresql-client -y

ADD ./django ./django
ADD ./docker ./docker
COPY --from=builder /usr/src/app/django/podscription-project/static/dist ./django/podscription-project/static/dist

FROM base as prod
EXPOSE 8888
RUN chmod +x ./docker/django/entry.sh

# ENTRYPOINT tail -f /dev/null
CMD ./docker/django/entry.sh
