from django import forms
from .models import StudentDetail, FacultyDetail
from django.contrib.auth.models import User,Group
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentDetail
        exclude = ['user',	]


class FacultyForm(forms.ModelForm):

    class Meta:
        model = FacultyDetail
        exclude = ['user',	]

class SignupForm(forms.ModelForm):

	class Meta:
		model = get_user_model()
		fields = ['username','email','groups']

	def signup(self, request, user):
		g = Group.objects.get(id=request.POST.get('groups'))
		user.groups.add(g)
		user.save()
