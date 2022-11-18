FROM python:3.10-slim

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
RUN python3 -m playwright install

ENTRYPOINT scrapyd

