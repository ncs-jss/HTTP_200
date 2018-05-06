from django.conf.urls import url
from newsletters import views

urlpatterns = [
    url(r'upload_newsletter/$', views.upload_newsletter, name="upload_newsletter"),
    url(r'(\d+)/$', views.show_letters, name="show_letters"),
    url(r'(?P<dept>[\w+-]+)/$', views.list_papers, name="list_papers"),
    url(r'$', views.list_departments, name="list_departments"),
]
