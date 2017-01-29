from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^student_profile_data/(?P<user_id>[0-9]+)/$', views.student_profile_data, name='student_profile_data'),
]
