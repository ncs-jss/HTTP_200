from django.conf.urls import url
from profiles.views import UserProfile

urlpatterns = [
    url(r'^(?P<user_id>.*)/$', UserProfile.as_view(), name="user-profile"),
]
