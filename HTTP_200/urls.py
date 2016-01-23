from django.conf.urls import url, include, patterns
from django.contrib.auth.decorators import login_required as auth
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from profiles.views import UserProfile, Home, EditProfile, FaqDisplayView
import settings
from django.conf.urls import handler404, handler500

handler404 = 'profiles.views.bad_request_404'
handler500 = 'profiles.views.bad_request_500'

urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^notices/', include('notices.urls')),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^api/', include('feeds.urls')),
    url(r'^token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^tokenverify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('profiles.urls')),
    url(r'^faq/$',  FaqDisplayView.as_view(), name="faq"),
    url(r'^messages/', include('message.urls')),
    # url(r'', include('rest_framework.urls', namespace='rest_framework'))
]

# For development environment

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}),
                            url(r'^plate/', include('django_spaghetti.urls')),
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
