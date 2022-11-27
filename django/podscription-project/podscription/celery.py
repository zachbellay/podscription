from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "podscription.settings")
app = Celery("podscription")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(['podscription.tasks'])

app.conf.result_chord_join_timeout = 900
app.conf.result_chord_retry_interval = 5
app.conf.result_expires = timedelta(days=3)

print('loading celery.py')


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


# @app.task()
# def test(arg):
#     print(arg)

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):

#     print("setup_periodic_tasks")
#     sender.add_periodic_task(3.0, test.s('hello'), name='add every 10')

