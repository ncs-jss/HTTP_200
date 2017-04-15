from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^student_profile_data/(?P<student_id>[0-9]+)/$', views.student_profile_data, name='student_profile_data'),
    url(r'^faculty_profile_data/(?P<faculty_id>[0-9]+)/$', views.faculty_profile_data, name='faculty_profile_data'),
]
