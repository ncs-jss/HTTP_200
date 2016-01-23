from django.conf.urls import url
from message.views import MessageView

urlpatterns = [
    url(r'', MessageView.as_view(), name='message_list'),
]
