from django.urls import path, include
from .consumers import ChatConsumer
from channels.routing import ProtocolTypeRouter, URLRouter

websocket_urlpatterns = [
    path('', ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(websocket_urlpatterns),
})