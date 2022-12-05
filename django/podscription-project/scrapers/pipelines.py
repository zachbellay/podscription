# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import asyncio
import aiohttp
import scrapy
# import whisper
from threading import Lock
import psycopg2
from api.models import PodcastEpisode
import tempfile
import concurrent.futures

# from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async

# class ScrapersPipeline:
#     def process_item(self, item, spider):
#         return item


# class AudioDownloadPipeline:
#     async def process_item(self, item, spider):
#         adapter = ItemAdapter(item)

#         if adapter.get("audio_url"):

#             async with aiohttp.request("GET", adapter.get("audio_url")) as response:
#                 audio_data = await response.read()

#             f = tempfile.NamedTemporaryFile(dir=spider.temp_dir.name, delete=False)
#             f.write(audio_data)

#             adapter["audio_data_path"] = f.name
#             return item
#         else:
#             raise scrapy.exceptions.DropItem("Missing audio_url")


# class TranscribeAudioPipeline:

#     model = whisper.load_model("base")
#     # lock = asyncio.Lock()
#     worker = concurrent.futures.ProcessPoolExecutor(max_workers=1)

#     def _sync_transcribe(self, audio_data_path: str):
#         return self.model.transcribe(
#             audio_data_path,
#             language="en",
#             without_timestamps=True,
#         )

#     async def get_podcast_episodes(self, details_url: str):
#         podcasts = await sync_to_async(list)(PodcastEpisode.objects.filter(details_url=details_url))

#     async def transcribe(self, audio_data_path: str):
#         with self.worker as worker:
#             loop = asyncio.get_event_loop()
#             return await loop.run_in_executor(worker, self._sync_transcribe, audio_data_path)

#     async def process_item(self, item, spider):
#         adapter = ItemAdapter(item)

#         if adapter.get('details_url'):
#             existing_podcast = await self.get_podcast_episodes(adapter.get('details_url'))

#             if existing_podcast and existing_podcast.transcription is not None:
#                 raise scrapy.exceptions.DropItem("Podcast already transcribed")

#         if adapter.get("audio_data_path"):

#             # transcription = None

#             async with self.lock:
#                 transcription = self.transcribe(adapter.get("audio_data_path"))
#                 # with concurrent.futures.ProcessPoolExecutor(max_workers=1) as pool:
            
#                 #     future = pool.submit(self.transcribe, adapter.get("audio_data_path"))
#                 #     result = concurrent.futures.wait(future)
#                 #     transcription = result.result()
#                 # results = [future.result() for future in futures]
#                 # transcription = results[0]
            
#             adapter["transcription"] = transcription["text"]
#             return item


# class SaveToDatabasePipeline:

# #     async def get_podcast_episodes(self, details_url: str):
# #         podcasts = await sync_to_async(list)(PodcastEpisode.objects.filter(details_url=details_url))

#     def process_item(self, item, spider):
#         # item.save(commit=False)
#         return item

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class DuplicatesPipeline:

    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['details_url'] in self.urls_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.urls_seen.add(adapter['details_url'])
            return item



class SaveToDatabasePipeline:


    async def process_item(self, item, spider):
        save = sync_to_async(item.save)
        result =  await save()
        return result

