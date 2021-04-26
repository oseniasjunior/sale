from celery import shared_task
from gevent.time import sleep

from core import models


@shared_task(bind=True, queue='default')
def process_long_task(self, loop_number: int):
    for item in range(0, loop_number):
        print(f'{item} de {loop_number}')
        models.Zone.objects.create(name=f'Zona {item}')


@shared_task(bind=True, queue='schedule_task')
def schedule_task(self):
    from datetime import datetime
    print(f'schedule_task at {datetime.today()}')
