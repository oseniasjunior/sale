from urllib import parse

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ConsumerBase(AsyncJsonWebsocketConsumer):

    def get_query_params(self):
        query_string = self.scope['query_string'].decode()
        return dict(parse.parse_qsl(query_string))

    def get_group_name(self):
        raise NotImplementedError('You must create subclasses and implement this method')

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(self.get_group_name(), self.channel_name)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.get_group_name(), self.channel_name)

    async def group_message(self, event):
        await self.send_json(content=event['content'])

    async def receive_json(self, event, **kwargs):
        await self.send_json(content=event['content'])


class ChatConsumer(ConsumerBase):

    def get_group_name(self):
        return 'chat'
