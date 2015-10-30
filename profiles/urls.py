from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required as auth
from profiles.views import UserProfile, EditProfile

urlpatterns = [
    url(r'(?P<slug>.*)/edit',  EditProfile.as_view(), name="edit-profile"),
    url(r'(?P<user_id>.*)/',  UserProfile.as_view(), name="user-profile"),

]
