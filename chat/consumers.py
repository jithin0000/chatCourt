import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404

from chat.models import Message
from customuser.models import MyUser
from case.models import Case


class ChatConsumer(WebsocketConsumer):
    case_number =""
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.case_number = self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()


    def fetch_last_messages(self,data):
        messages = Message.last_10_messages(self)
        content = {
            "messages" :self.messages_to_json(messages),
            "command" : "messages"
        }
        self.send_message(content)

    def new_message(self, data):
        author = get_object_or_404(MyUser, pk = data['from'])
        case = get_object_or_404( Case, case_number = self.case_number)
        print(case)
        message = Message.objects.create( message=data['message'], author= author , case= case)
        content = {
            'message' : self.message_to_json(message),
            'command' : 'new_message'
        }
        return self.send_message(content)

    commands = {
        "fetch_messages": fetch_last_messages,
        "new_message" : new_message
    }

    def messages_to_json(self, messages):
        result =[]
        for m in messages:
            result.append(self.message_to_json(m))
        return result

    def message_to_json(self, message):
        return {
            'author' : "jithin",
            'message' : message.message,
            'timestamp' : str(message.timestamp)
        }


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

        # Send message to room group
    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))