from notices.models import Notice
from django import forms

class NoticeCreateForm(forms.ModelForm):
	class Meta:
		model = Notice
		exclude = ('faculty',)
