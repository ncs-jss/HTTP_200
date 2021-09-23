from django import forms
from .models import EmailDetail


class EmailForm(forms.ModelForm):

    class Meta:
        model = EmailDetail
        fields = ['email_purpose', 'attachment']
        exclude = ['user', ]
