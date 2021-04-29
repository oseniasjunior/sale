def send_channel_message(group_name: str, content: dict) -> None:
    from asgiref.sync import async_to_sync
    from channels.layers import get_channel_layer

    channel_layer = get_channel_layer()
    print(group_name)
    async_to_sync(channel_layer.group_send)(group_name, {
        "type": "group.message",
        "content": content
    })
