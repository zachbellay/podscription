from datetime import date
from ninja import Schema


class PodcastIn(Schema):
    name: str
    author: str
    url: str

class PodcastOut(Schema):
    id: int
    name: str
    author: str
    url: str