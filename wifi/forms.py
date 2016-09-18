from django import forms
from .models import WifiDetail


class WifiForm(forms.ModelForm):

    class Meta:
        model = WifiDetail
        fields = ['laptop_mac_address', ]
        exclude = ['user', ]
