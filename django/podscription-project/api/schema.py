from datetime import date
from typing import Dict, List, Optional

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
    # audio_url: str
    resolved_audio_url: str
    details_url: str
    slug: str
    duration: int
    transcription: Optional[List[Dict[str, str]]]


class PodcastEpisodeLightOut(Schema):
    id: int
    podcast_name: str
    date: date
    title: str
    description: str
    # audio_url: str
    resolved_audio_url: str
    details_url: str
    slug: str
    duration: int


class PodcastSearchResultOut(Schema):
    episode_id: int
    podcast: PodcastOut
    headline: str
