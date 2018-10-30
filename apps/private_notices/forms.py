from django import forms
from private_notices.models import PrivateNotice


class PostForm(forms.ModelForm):

    class Meta:
        model = PrivateNotice
        fields = ('reciever', 'pnotice',)
