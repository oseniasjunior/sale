from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sale.settings')

app = Celery('sale')
app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default', delivery_mode=1),
    Queue('schedule_task', Exchange('schedule_task'), routing_key='schedule_task', delivery_mode=1),
)

app.conf.beat_schedule = {
    'schedule_task': {
        'task': 'core.tasks.schedule_task',
        'schedule': 10
    },
}

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
