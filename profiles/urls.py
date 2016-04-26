from django.conf.urls import url
from profiles.views import UserProfile, EditProfile

urlpatterns = [
    # url(r'^(?P<slug>.*)/$', EditProfile.as_view(), name="edit-profile"),
    url(r'^(?P<user_id>.*)/$', UserProfile.as_view(), name="user-profile"),
]
