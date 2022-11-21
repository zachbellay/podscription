FROM python:3.6-slim

ENV DEBIAN_FRONTEND noninteractive
ENV SCRAPY_PROJECTS_DIR /src/projects


RUN apt update && apt install git -y

RUN mkdir /app
WORKDIR /app

COPY ./docker/scrapyd-web/requirements.txt .

RUN python3 -m pip install -r requirements.txt

RUN python3 -m pip install --upgrade git+https://github.com/my8100/scrapydweb.git

COPY ./scrapers /src/projects/scrapers/scrapers
COPY ./scrapy.cfg /src/projects/scrapers

ENTRYPOINT ["scrapydweb"]
# ENTRYPOINT tail -f /dev/null