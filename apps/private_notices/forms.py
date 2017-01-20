from django import forms
from private_notices.models import PrivateNotice, Notification


class PostForm(forms.ModelForm):

    class Meta:
        model = PrivateNotice
        fields = ('reciever', 'pnotice',)
