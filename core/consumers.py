# core/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        user1, user2 = self.scope['url_route']['kwargs']['room_name'].split('-')
        self.room_group_name = f'chat_{ "-".join(sorted([user1, user2])) }'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        from django.contrib.auth.models import User  # 👈 Explicit import here explicitly (important)
        from .models import ChatMessage  # 👈 Explicit import clearly moved in here explicitly
        
        data = json.loads(text_data)
        sender = self.scope["user"]
        receiver_username = data['receiver']
        receiver = await database_sync_to_async(User.objects.get)(username=receiver_username)

        message = data['message']

        # explicitly save message to DB
        chat_message = ChatMessage(sender=sender, receiver=receiver, message=message)
        await database_sync_to_async(chat_message.save)()

        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "chat_message", "message": message, "sender": sender.username}
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender']
        }))