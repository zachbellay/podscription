FROM python as builder

RUN pip install scrapyd-client

WORKDIR /build

COPY scrapers .
COPY scrapy.cfg .

RUN scrapyd-deploy --build-egg=scraper.egg

############################################
############################################
############################################

FROM python:3.10-slim

COPY ./docker/scrapyd/requirements.txt .
RUN python3 -m pip install -r requirements.txt
RUN python3 -m playwright install

RUN mkdir -p /src/eggs/scraper
COPY --from=builder /build/scraper.egg /src/eggs/scraper/1_0.egg

ENTRYPOINT scrapyd

