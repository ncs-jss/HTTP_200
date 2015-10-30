from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required as auth
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from profiles.views import UserProfile, Home, EditProfile

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include('feeds.urls')),
    url(r'^token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^tokenverify/', 'rest_framework_jwt.views.verify_jwt_token'),
	    url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('rest_framework.urls', namespace='rest_framework'))

    url(r'$/',  Home.as_view(), name="home"),
    url(r'user/(?P<slug>.*)/edit',  EditProfile.as_view(), name="edit-profile"),
    url(r'user/(?P<user_id>.*)/',  UserProfile.as_view(), name="user-profile"),

]
