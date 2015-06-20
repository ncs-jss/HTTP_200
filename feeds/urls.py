from django.conf.urls import include, url
from django.contrib import admin
from feeds import views

urlpatterns = [
    url(r'^$','feeds.views.home',name="home"),
    # url(r'^admin/', include(admin.site.urls)),

]

'''
the below module import is used for importing the foramt type in which we 
the data like json or xml
'''
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns += patterns('feeds.serializers',
    url(r'^api/student/$', views.StudentList.as_view()),
    url(r'^api/student/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
    url(r'^api/faculty/$', views.FacultyList.as_view()),
    url(r'^api/faculty/(?P<pk>[0-9]+)/$', views.FacultyDetail.as_view()),
    url(r'^api/notice/$', views.NoticeList.as_view()),
    url(r'^api/notice/(?P<pk>[0-9]+)/$', views.NoticeDetail.as_view()),
    url(r'^api/scheduled_notce/$', views.ScheduleNoticeList.as_view()),
    url(r'^api/scheduled_notce/(?P<pk>[0-9]+)/$', views.ScheduleNoticeDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

