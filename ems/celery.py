from __future__ import absolute_import, unicode_literals
import imp
import os
from time import timezone

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE','ems.settings')

app = Celery('ems')
app.conf.enable_utc = False

app.conf.update(timezone = 'Africa/Lagos')

app.config_from_object('django.conf:settings', namespace='CELERY')

# CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    # 'Schedule Bills Creation':{
    #     'task':'bills.task.create_bills_for_all',
    #     'schedule':crontab(hour=12,minute=54),
    #     'args': ()
    # }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
