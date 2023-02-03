import random
import re
import string
from datetime import datetime, timedelta

import bleach

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


# def unique_slug_generator(instance, slug_attr, new_slug = None):
#     if new_slug is not None:
#         slug = new_slug
#     else:
#         slug = slugify(getattr(instance, slug_attr))
#     Klass = instance.__class__
#     qs_exists = Klass.objects.filter(slug = slug).exists()
#     if qs_exists:
#         new_slug = "{slug}-{randstr}".format(
#             slug = slug, randstr = random_string_generator(size = 4))

#         return unique_slug_generator(instance, slug_attr, new_slug = new_slug)
#     return slug


def unique_slug_generator(instance, slug_attr, filter_args=None, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(getattr(instance, slug_attr))
    Klass = instance.__class__

    if filter_args is None:
        qs_exists = Klass.objects.filter(slug=slug).exists()
    else:
        qs_exists = Klass.objects.filter(slug=slug, **filter_args).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4)
        )

        return unique_slug_generator(
            instance, slug_attr, filter_args=filter_args, new_slug=new_slug
        )
    return slug


# def group_text_by_time_window(result: dict, time_window_size: int = 30):
#     """
#     Group text output from OpenAI whisper into time windows
#     :param result: dict, output from OpenAI whisper model
#     :param time_window_size: int, size of time window in seconds

#     :return: dict, start time in seconds as key, text as value
#     """

#     # get transcript segments and their start times
#     seg_starts = [seg["start"] for seg in result["segments"]]
#     seg_text = [seg["text"] for seg in result["segments"]]

#     time_windows = {}

#     # group text into buckets
#     for time, text in zip(seg_starts, seg_text):
#         time_window = int(time // time_window_size)

#         if time_window not in time_windows:
#             time_windows[time_window] = [text]
#         else:
#             time_windows[time_window].append(text)
#     final_times = {}

#     # merge all pieces of text in each bucket
#     # and convert time window to seconds
#     for time, text in time_windows.items():
#         final_times[int(time * time_window_size)] = "".join(text)

#     return final_times


def group_text_by_time_window(result: dict, duration: int, time_window_size: int = 30):
    """
    Group text output from OpenAI whisper into time windows
    :param result: dict, output from OpenAI whisper model
    :param time_window_size: int, size of time window in seconds

    :return: dict, start time in seconds as key, text as value
    """
    # get transcript segments and their start times
    seg_starts = [seg["start"] for seg in result["segments"]]
    seg_text = [seg["text"] for seg in result["segments"]]

    time_windows = {}

    # group text into buckets
    for time, text in zip(seg_starts, seg_text):
        time_window = int(time // time_window_size)

        if time_window not in time_windows:
            time_windows[time_window] = [text]
        else:
            time_windows[time_window].append(text)
    final_times = {}

    # create lists of start and ends times
    starts = [index * time_window_size for index in time_windows.keys()]
    ends = starts[1:] + [duration]

    final_result = []

    # create list of texts with startime and end timex
    for ((index, text), (start, end)) in zip(time_windows.items(), zip(starts, ends)):
        final_result.append({"start": start, "end": end, "text": "".join(text)})

    return final_result


def duration_to_seconds(duration_str):
    try:
        # Try to parse the duration string as an integer
        duration_in_seconds = int(duration_str)
    except ValueError:
        # If the duration string is not an integer, parse it as a time
        duration = datetime.strptime(duration_str, "%H:%M:%S")

        # Convert the duration to a timedelta object
        duration = timedelta(
            hours=duration.hour, minutes=duration.minute, seconds=duration.second
        )

        # Extract the total number of seconds from the timedelta object
        duration_in_seconds = duration.total_seconds()

    return duration_in_seconds

def clean_description(text: str)->str:
    # remove urls that are inside [], e.g. [https://www.example.com]
    text = re.sub(r'\[https?://[^\]]+\]', '', text)

    # linkify naked urls
    text = bleach.linkify(text)

    # remove unsafe tags
    text = bleach.clean(text, tags=list(bleach.sanitizer.ALLOWED_TAGS)+['p'], strip=True)

    return text