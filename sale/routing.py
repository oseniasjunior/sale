from django.urls import path

from core import consumers as core_consumers

urlrouter = [
    path('chat/', core_consumers.ChatConsumer.as_asgi()),
]
