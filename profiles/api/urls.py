from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserLoginAPIView,
	)

urlpatterns = [
	url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	
]