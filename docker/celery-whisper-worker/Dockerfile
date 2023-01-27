FROM python:3.10-slim as builder

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt update && \
    apt install -y --no-install-recommends \
        gcc \
        g++ \
        build-essential  \
        wget \
        ffmpeg \
        libpq-dev \
        git \
    && rm -rf /var/lib/apt/lists/*

USER root
RUN useradd -ms /bin/bash celery && \
    usermod -a -G celery celery && \
    usermod -a -G celery root

WORKDIR /usr/src/app
COPY ./docker/celery-whisper-worker/requirements.txt ./requirements.txt

RUN python -m venv --copies /usr/src/app/venv
RUN . /usr/src/app/venv/bin/activate && pip install --no-cache -r ./requirements.txt

# ================================

FROM python:3.10-slim as prod

ENV PATH="/usr/src/app/venv/bin:$PATH"
WORKDIR /usr/src/app

RUN apt update \
    && apt install -y --no-install-recommends \
        libpq-dev \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*


COPY ./docker ./docker

COPY ./docker/celery/celeryd /etc/init.d/
COPY ./docker/celery/celerybeat /etc/init.d/
COPY ./docker/celery/config/celeryd /etc/default/

RUN chmod 755 /etc/init.d/celeryd && \
    chmod 755 /etc/init.d/celerybeat && \
    chmod 640 /etc/default/celeryd && \
    chmod +x ./docker/celery-worker/entry.sh

COPY ./django ./django

COPY --from=builder /usr/src/app/venv /usr/src/app/venv/

RUN python -c "import whisper; whisper.load_model('base')"

ENTRYPOINT ["./docker/celery-whisper-worker/entry.sh"]
