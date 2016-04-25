from django.conf.urls import url, include, patterns
from django.contrib import admin
from profiles.views import Home, FaqDisplayView, about, contact
import settings

urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^notices/', include('notices.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^tokenverify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('profiles.urls')),
    url(r'^faq/$', FaqDisplayView.as_view(), name="faq"),
    url(r'^pnotices/', include('private_notices.urls')),
    url(r'^about/$', about, name='about'),
    url(r'^add/$', contact, name='contact'),
    # url(r'^api/', include('feeds.urls')),
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
