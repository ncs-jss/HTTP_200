from django import forms
from . import models


class upload_letter_form(forms.ModelForm):
	'''
	This validates the newsletter data input by user.
	'''
	class Meta:
		model = models.papers
		fields = ['name', 'year', 'paper']
		exclude = ['department', 'uploaded_by']
