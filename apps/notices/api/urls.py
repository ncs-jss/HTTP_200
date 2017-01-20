from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'notice_by_pk/(?P<pk>[0-9]+)/$', NoticeListViewSet.as_view(ListCreateMapper), name='notice-list'),
    url(r'notices_create/$', NoticeCreateViewSet.as_view(), name='notice-create'),
    url(r'notice_list/$', NoticeListViewSet.as_view(ListCreateMapper), name='notice-list'),

]


