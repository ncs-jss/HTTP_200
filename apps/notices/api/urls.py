from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'notice_by_pk/(?P<notice_pk>[0-9]+)/$', views.get_notice_by_pk, name='get_notice_by_pk'),
    url(r'notice_list/$', views.get_notice_by_list, name='get_notice_by_list'),
    url(r'notice_create/$', views.create_notice, name='create_notice'),

]
