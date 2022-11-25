FROM python as builder

RUN pip install scrapyd-client

WORKDIR /build

ADD ./scrapers/docker/scrapyd/scrapyd.conf .

ADD ./django/podscription-project ./django/podscription-project
ADD ./scrapers/scrapers ./scrapers/scrapers
ADD ./scrapers/scrapy.cfg ./scrapers/scrapy.cfg

RUN cd scrapers && scrapyd-deploy --build-egg=scraper.egg



FROM python:3.10-slim

RUN apt update && apt install -y gcc build-essential libpq-dev

WORKDIR /usr/src/app

ADD ./scrapers/docker/scrapyd/requirements.txt .
RUN python3 -m pip install -r requirements.txt
RUN python3 -m playwright install
RUN playwright install-deps

# ADD ./scrapers/docker/scrapyd/scrapyd.conf .

# ADD ./django/podscription-project ./django/podscription-project
# ADD ./scrapers/scrapers ./scrapers/scrapers
# ADD ./scrapers/scrapy.cfg ./scrapers/scrapy.cfg
WORKDIR /src/eggs/scraper
# RUN mkdir -p /src/eggs/scraper
COPY --from=builder /build/scrapers/scraper.egg eggs/the-daily-podcast/1_0.egg
ADD ./scrapers/docker/scrapyd/scrapyd.conf .
# ENTRYPOINT tail -f /dev/null
ENTRYPOINT scrapyd






############################################
############################################
############################################

# FROM python:3.10-slim

# COPY ./docker/scrapyd/requirements.txt .
# RUN python3 -m pip install -r requirements.txt
# RUN python3 -m playwright install

# RUN mkdir -p /src/eggs/scraper
# COPY --from=builder /build/scraper.egg /src/eggs/scraper/1_0.egg

# ENTRYPOINT scrapyd



