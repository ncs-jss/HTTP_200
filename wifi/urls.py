from django.conf.urls import url
from wifi.views import StudentWifiForm, FacultyWifiForm, excel_writer

urlpatterns = [

	url(r'^student/$', StudentWifiForm.as_view(), name="student-wifi"),
	url(r'^faculty/$', FacultyWifiForm.as_view(), name="faculty-wifi"),
	url(r'^download_excel/$', excel_writer.as_view(), name="excel_writer"),
]
