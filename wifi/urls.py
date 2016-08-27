from django.conf.urls import url, include, patterns
from wifi.views import StudentWifiForm, FacultyWifiForm

urlpatterns = [

	url(r'^student/$' ,StudentWifiForm.as_view(), name="student-wifi" ),
	url(r'^faculty/$', FacultyWifiForm.as_view(), name="faculty-wifi"),
]