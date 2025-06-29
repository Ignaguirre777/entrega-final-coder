from django.urls import path
from .views import inbox, sent_messages, send_message

urlpatterns = [
    path('inbox/', inbox, name='messenger-inbox'),
    path('sent/', sent_messages, name='messenger-sent'),
    path('send/', send_message, name='messenger-send'),
]
