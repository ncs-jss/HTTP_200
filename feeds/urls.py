from django.conf.urls import include, url, patterns
from django.contrib import admin
from rest_framework import renderers
from feeds.views import *


'''
	The below `notice_list_only` is for displaying the small part of all notices that us used to 
	display the specific details on the dashboard.
''' 
notice_list_only = NoticeListViewSet.as_view({
	'get': 'list'
})

notice_list = NoticeViewSet.as_view({
	'get': 'list',
	'post': 'create'
})

notice_detail = NoticeViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
})

user_list = UserViewSet.as_view({
	'get': 'list'
})
user_detail = UserViewSet.as_view({
	'get': 'retrieve'
})

student_list = StudentViewSet.as_view({
	'get': 'list'
})
student_detail = StudentViewSet.as_view({
	'get': 'retrieve'
})
faculty_list = FacultyViewSet.as_view({
	'get': 'list'
})
faculty_detail = FacultyViewSet.as_view({
	'get': 'retrieve'
})

urlpatterns = [
	# url(r'^$','feeds.views.home',name="home"),
	# url(r'^$','feeds.views.home',name="home"),
	# url(r'^admin/', include(admin.site.urls)),
]

'''
the below module import is used for importing the foramt type in which we 
the data like json or xml
'''
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns += patterns('feeds.serializers',
	url(r'^$', api_root),
	url(r'^api/student/$', student_list, name = "student-list"),
	url(r'^api/student/(?P<pk>[0-9]+)/$', student_detail, name = "student-detail"),
	url(r'^api/faculty/$', faculty_list, name = "faculty-list"),
	url(r'^api/faculty/(?P<pk>[0-9]+)/$', faculty_detail, name = "faculty-detail"),
	url(r'^api/notice/$', notice_list, name = "notice-list"),
	url(r'^api/notice/(?P<pk>[0-9]+)/$', notice_detail, name = "notice-detail"),
	url(r'^api/notice/list/$', notice_list_only, name = "notice-list-only"),
	url(r'^users/$', user_list, name = "user-list"),
	url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name = "user-detail"),
	# url(r'^check/$', views.check.as_view()),
)

urlpatterns += [
	url(r'^api-auth/', include('rest_framework.urls',
		namespace='rest_framework')),
]
urlpatterns = format_suffix_patterns(urlpatterns)