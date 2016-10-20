from django.conf.urls import url

from .views import (
    NoticeListAPIView,
)

urlpatterns = [
    url(r'^', NoticeListAPIView.as_view(), name='list'),

]
