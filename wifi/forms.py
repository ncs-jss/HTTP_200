from django import forms
from .models import WifiDetail
from django.contrib.auth.models import User


class WifiForm(forms.ModelForm):

    class Meta:
        model = WifiDetail
        fields = ['laptop_mac_address',]
        exclude = ['user',]
        