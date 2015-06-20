from django.conf.urls import url, include
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('feeds.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api', include('rest_framework.urls', namespace='rest_framework'))
]
