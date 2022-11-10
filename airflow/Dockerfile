# use this to get the list of system level dependencies that need to be installed in the container
FROM debian:bullseye-slim as build

RUN apt update && apt install python3 python3-pip -y
RUN python3 -m pip install playwright
RUN python3 -m playwright install --with-deps --dry-run | grep "sh -c" >> root/playwright.install.sh

# build the actual image
FROM apache/airflow:2.4.2

ENV DEBIAN_FRONTEND noninteractive

COPY --from=build /root/playwright.install.sh /root/playwright.install.sh

USER root
RUN bash /root/playwright.install.sh
RUN apt update && apt install git ffmpeg htop -y

RUN curl -L https://github.com/xxxserxxx/gotop/releases/download/v4.2.0/gotop_v4.2.0_linux_amd64.deb -o gotop.deb && dpkg -i gotop.deb && rm gotop.deb

USER airflow

RUN python3 -m pip install playwright
RUN python3 -m playwright install

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

RUN python -c 'import whisper; whisper.load_model("base")'


# docker run --rm -it airflow-base:latest bash
