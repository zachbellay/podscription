FROM python:3.10-slim
EXPOSE 5555

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt update && apt install libpq-dev -y

USER root
RUN useradd -ms /bin/bash celery
RUN usermod -a -G celery celery
RUN usermod -a -G celery root

WORKDIR /usr/src/app

COPY ./docker/celery-flower/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./docker ./docker
COPY ./django ./django

COPY ./docker/celery/celeryd /etc/init.d/
COPY ./docker/celery/celerybeat /etc/init.d/
COPY ./docker/celery/config/celeryd /etc/default/

RUN chmod 755 /etc/init.d/celeryd && \
    chmod 755 /etc/init.d/celerybeat && \
    chmod 640 /etc/default/celeryd && \
    chmod +x ./docker/celery-flower/entry.sh

ENTRYPOINT ["./docker/celery-flower/entry.sh"]
# ENTRYPOINT tail -f /dev/null 
