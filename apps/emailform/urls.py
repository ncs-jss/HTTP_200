from django.conf.urls import url
from emailform.views import StudentEmailForm, email_excel_writer


urlpatterns = [
    url(r'^email$', StudentEmailForm.as_view(), name="student-email"),
    url(r'^download_excel$', email_excel_writer.as_view(), name="email_excel_writer"),
]
