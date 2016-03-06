from django.conf.urls import url
from private_notices.views import PrivateNoticeView, NotificationView #, CreatePrivateNoticeView

urlpatterns = [
    url(r'^$', PrivateNoticeView.as_view(), name='PrivateNotice_list'),
    #url(r'^new$', CreatePrivateNoticeView.as_view(), name='new_PrivateNotice'),
    url(r'^(?P<user_id>.*)/notification/$',  NotificationView.as_view(), name='notification'),
]
