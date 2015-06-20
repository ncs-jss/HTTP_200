from django.conf.urls import include, url
from django.contrib import admin
# from feeds.views import *

urlpatterns = [
    url(r'^$','feeds.views.home',name="home"),
    # url(r'^admin/', include(admin.site.urls)),

]