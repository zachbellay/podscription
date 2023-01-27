FROM node:19-slim as frontend-builder

WORKDIR /usr/src/app

COPY package.json package-lock.json tsconfig.json tsconfig.node.json tailwind.config.cjs postcss.config.cjs vite.config.ts openapitools.json ./

RUN npm install

COPY ./django/podscription-project/static/src ./django/podscription-project/static/src

RUN npm run build

# ================================

FROM python:3.10 as django-builder

SHELL ["/bin/bash", "-c"] 

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        build-essential \
        wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ./docker/django/requirements.txt ./requirements.txt

RUN python -m venv --copies /usr/src/app/venv
RUN . /usr/src/app/venv/bin/activate && pip install --no-cache -r ./requirements.txt

# ================================

FROM python:3.10-slim as prod

ENV PATH="/usr/src/app/venv/bin:$PATH"
WORKDIR /usr/src/app

RUN apt update \
        && apt install -y --no-install-recommends \ 
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./django ./django
COPY ./docker ./docker

COPY --from=django-builder /usr/src/app/venv /usr/src/app/venv/
COPY --from=frontend-builder /usr/src/app/django/podscription-project/static/dist ./django/podscription-project/static/dist

EXPOSE 8888
RUN chmod +x ./docker/django/entry.sh

CMD ./docker/django/entry.sh
