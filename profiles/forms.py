from django import forms
from .models import StudentDetail

class StudentForm(forms.ModelForm):
	class Meta:
		model = StudentDetail
		fields = ['univ_roll_no', ]
