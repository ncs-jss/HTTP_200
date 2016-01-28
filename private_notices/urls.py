from django.conf.urls import url
from private_notices.views import PrivateNoticeView, CreatePrivateNoticeView

urlpatterns = [
    url(r'', PrivateNoticeView.as_view(), name='PrivateNotice_list'),
    url(r'^new$', CreatePrivateNoticeView.as_view(), name='new_PrivateNotice'),
]
