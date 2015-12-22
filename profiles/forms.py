from django import forms
from .models import StudentDetail, FacultyDetail
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentDetail
        exclude = ['user',	]


class FacultyForm(forms.ModelForm):

    class Meta:
        model = FacultyDetail
        exclude = ['user',	]
