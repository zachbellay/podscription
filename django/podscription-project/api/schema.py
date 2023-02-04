from datetime import datetime
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
    date: datetime
    title: str
    description: str
    resolved_audio_url: str
    details_url: str
    slug: str
    duration: int
    transcription: Optional[List[Dict[str, str]]]


class PodcastEpisodeLightOut(Schema):
    id: int
    podcast_name: str
    date: datetime
    title: str
    description: str
    resolved_audio_url: str
    details_url: str
    slug: str
    duration: int


class PodcastEpisodeSearchResultOut(Schema):
    id: int
    podcast_name: str
    podcast: PodcastOut
    date: datetime
    title: str
    description: str
    resolved_audio_url: str
    details_url: str
    slug: str
    duration: int
    headline: str


# class SearchResultOut(Schema):
# pass
# episode_id: int
# podcast: PodcastOut
# headline: str
