from datetime import date
from typing import List, Optional

from ninja import Schema


class PodcastOut(Schema):
    id: int
    name: str
    author: str
    url: str
    logo_url: str
    description: str
    website_url: str
    slug: str


class PodcastEpisodeOut(Schema):
    id: int
    podcast_name: str
    date: date
    title: str
    description: str
    audio_url: str
    details_url: str
    slug: str
    transcription: Optional[str]


class PodcastEpisodeLightOut(Schema):
    id: int
    podcast_name: str
    date: date
    title: str
    description: str
    audio_url: str
    details_url: str
    slug: str


class PodcastSearchResultOut(Schema):
    episode_id: int
    podcast: PodcastOut
    headline: str
