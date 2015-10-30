from django import forms
from .models import StudentDetail
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
	class Meta:
		model = StudentDetail
		exclude = ['user',	]