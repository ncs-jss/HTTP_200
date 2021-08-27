from django.conf.urls import url
from wifi.views import StudentWifiForm, FacultyWifiForm, StudentEmailForm, excel_writer, email_excel_writer


urlpatterns = [
    url(r'^faculty/$', FacultyWifiForm.as_view(), name="faculty-wifi"),
    url(r'^student/$', StudentWifiForm.as_view(), name="student-wifi"),
    url(r'^student/email$', StudentEmailForm.as_view(), name="student-email"),
    url(r'^download_excel/$', excel_writer.as_view(), name="excel_writer"),
    url(r'^download_excel/emails$', email_excel_writer.as_view(), name="email_excel_writer"),
]
