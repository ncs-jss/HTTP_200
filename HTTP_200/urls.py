from django.conf.urls import url, include, patterns
from django.contrib import admin
from allauth.account.views import login, logout
from profiles.views import Home, FaqDisplayView, about, Contact
import settings

urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^notices/', include('notices.urls')),
    url(r'^accounts/password/change/$', 'profiles.views.password_change', name='password_change'),
    url(r'^login/$', login, name="account_login"),
    url(r'^logout/$', logout, name="account_logout"),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^tokenverify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('profiles.urls')),
    url(r'^faq/$', FaqDisplayView.as_view(), name="faq"),
    url(r'^pnotices/', include('private_notices.urls')),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
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
