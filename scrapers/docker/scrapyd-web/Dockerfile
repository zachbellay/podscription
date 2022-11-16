FROM python:3.7-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install git -y

RUN pip install --upgrade git+https://github.com/my8100/scrapydweb.git

ENTRYPOINT scrapydweb