from rest_framework import routers

from django.conf.urls import url

from notices.api.views import (
    NoticeListViewSet,
    NoticeCreateViewSet,
    MyUploadedNoticeViewSet,
)

router = routers.SimpleRouter()

router.register(
    r'notices',
    NoticeListViewSet,
    base_name='notice'
)

ListCreateMapper = {
    'get': 'list',
}

urlpatterns = [
    url(r'notices/(?P<pk>[0-9]+)/$', NoticeListViewSet.as_view(ListCreateMapper), name='notice-list'),
    url(r'notices/$', NoticeListViewSet.as_view(ListCreateMapper), name='notice-list'),
    url(r'notices/create/$', NoticeCreateViewSet.as_view(), name='notice-create'),
    # url(r'notices/delete/(?P<pk>\d+)', NoticeCreateViewSet.as_view(), name='notice-delete'),
    # url(r'/myuploaded/notice/$', MyUploadedNoticeViewSet.as_view(), name='notice-myuploaded'),
    # url(r'share/?<pk>[0-9+]/$', NoticeListViewSet.as_view(ListCreateMapper), name='notice-share'),
]

urlpatterns += router.urls
