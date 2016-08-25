from django.conf.urls import url, include, patterns
from wifi.views import WifiForm


urlpatterns = [

	url(r'^' ,WifiForm.as_view(), name="wifi" ),
]