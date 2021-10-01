from django.conf.urls import url
from emailform.views import StudentEmailForm


urlpatterns = [
    url(r'^email$', StudentEmailForm.as_view(), name="student-email"),
]
