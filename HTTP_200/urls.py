# django imports
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
# allauth imports
from allauth.account.views import login, logout

# local file imports
from profiles.views import (Home,
                            FaqDisplayView,
                            about,
                            Contact,
                            BulkUser,
                            SingleUser,
                            password_change)


admin.site.site_header = "JSS InfoConnect Admin Interface"

urlpatterns = [
    # Web urls
    url(r'^$', Home.as_view(), name="home"),
    url(r'^notices/', include('notices.urls')),
    url(r'^accounts/password/change/$', password_change, name='password_change'),
    url(r'^login/$', login, name="account_login"),
    url(r'^logout/$', logout, name="account_logout"),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('profiles.urls')),
    url(r'^faq/$', FaqDisplayView.as_view(), name="faq"),
    # url(r'^pnotices/', include('private_notices.urls')),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    # url(r'^api/', include('feeds.urls')),
    # url(r'', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^students/create/single/$', SingleUser.as_view(), name='single_user_create'),
    url(r'^students/create/$', BulkUser.as_view(), name='bulk_students_create'),
    url(r'wifi/', include('wifi.urls')),

    # api urls
    # url(r'^api/profiles/', include("profiles.api.urls", namespace='profiles_api')),
    # url(r'^api/notices/', include("notices.api.urls", namespace='notices_api')),
    # url(r'^api/notifications/', include("notifications.api.urls", namespace='notifications_api')),
    url(r'^api/profiles/', include("profiles.api.urls")),
    url(r'^api/notices/', include("notices.api.urls")),
    url(r'^api/notifications/', include("notifications.api.urls")),
]

# For development environment
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += url(
#         '', include(
#             [
#                 url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#                     'document_root': settings.MEDIA_ROOT}),
#                 url(r'^dbschema/', include('django_spaghetti.urls')),
#                 url(r'^__debug__/', include(debug_toolbar.urls)),
#                 url(r'^api/docs/', include('rest_framework_docs.urls')),
#             ]
#         )
#     )
