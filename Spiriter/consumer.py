import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from Spiriter.llm_service import generate_content

class WSLeaderboardHandler(WebsocketConsumer):
    def connect(self):
        self.group_name = 'websocket_group'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def send_message(self, event):
        message = event['message']
        self.send(text_data=message)

class WSLLMHandler(WebsocketConsumer):
    def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user']
        async_to_sync(self.channel_layer.group_add)(
            self.user_id,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.user_id,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        question = data.get('message', 'Introduce yourself')
        print(question)

        from AdminPanel.models import Player
        from UserInterface.models import EndUser
        
        user = EndUser.objects.get(id=self.user_id)

        players = Player.objects.all()
        response = generate_content(question, players, user)
        
        # Send response back to the client
        self.send(text_data=json.dumps({
            'response': response,
            'question': question
        }))

    def llm_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))