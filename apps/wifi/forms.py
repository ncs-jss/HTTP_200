from django import forms
from .models import WifiDetail, EmailDetail


class WifiForm(forms.ModelForm):

    class Meta:
        model = WifiDetail
        fields = ['old_laptop_mac_address', 'new_laptop_mac_address', ]
        exclude = ['user', ]


class EmailForm(forms.ModelForm):

    class Meta:
        model = EmailDetail
        fields = ['email_purpose', 'attachment']
        exclude = ['user', ]
