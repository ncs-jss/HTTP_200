from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'notice_by_pk/(?P<notice_pk>[0-9]+)/$', views.get_notice_by_pk, name='get_notice_by_pk'),
    url(r'notice_list/$', views.get_notice_by_list, name='get_notice_by_list'),
    # url(r'notices_create/$', NoticeCreateViewSet.as_view(), name='notice-create'),

]
