FROM python:3.10-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install git curl ffmpeg htop -y

RUN curl -L https://github.com/xxxserxxx/gotop/releases/download/v4.2.0/gotop_v4.2.0_linux_amd64.deb -o gotop.deb && dpkg -i gotop.deb && rm gotop.deb

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

RUN python3 -m pip install playwright && \
    python3 -m playwright install

RUN python -c 'import whisper; whisper.load_model("base")'

ENTRYPOINT scrapyd

