from django.urls import re_path
from Spiriter.consumer import WSLeaderboardHandler, WSLLMHandler

websocket_urlpatterns = [
    re_path(r'ws/leaderboard/$', WSLeaderboardHandler.as_asgi()),
    re_path(r'ws/chat/(?P<user>\w+)/$', WSLLMHandler.as_asgi()),
]
