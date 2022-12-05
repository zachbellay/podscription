from datetime import date
from typing import List, Optional

from ninja import Schema


class PodcastOut(Schema):
    id: int
    name: str
    author: str
    url: str


class PodcastEpisodeOut(Schema):
    id: int
    date: date
    title: str
    description: str
    audio_url: str
    details_url: str
    transcription: Optional[str]
