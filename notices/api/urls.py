from django.conf.urls import url
from django.contrib import admin

from .views import (
	NoticeListAPIView,
	)

urlpatterns = [
	url(r'^', NoticeListAPIView.as_view(), name='list'),
	
]