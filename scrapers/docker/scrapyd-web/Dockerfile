FROM python:3.6-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install git -y

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

RUN python3 -m pip install --upgrade git+https://github.com/my8100/scrapydweb.git

# ENTRYPOINT (scrapydweb || true) && tail -f /dev/null

# CMD [ "scrapydweb" ]
# ENTRYPOINT ["scrapydweb"]
ENTRYPOINT tail -f /dev/null


# DOCKER_DEFAULT_PLATFORM=linux/amd64 docker run web --volume ./scrapyd-web-volume:/app