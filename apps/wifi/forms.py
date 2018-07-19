from django import forms
from .models import WifiDetail


class WifiForm(forms.ModelForm):

    class Meta:
        model = WifiDetail
        fields = ['old_laptop_mac_address', 'new_laptop_mac_address', ]
        exclude = ['user', ]
