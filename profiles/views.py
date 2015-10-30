from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

from .models import StudentDetail
from .forms import StudentForm
# Create your views here.
class Home(View):
	'''
	'''
	def get(self,request):
		template_name = 'index.html'
		return render(request, template_name)

class UserProfile(View):
	'''
	'''
	def get(self,request, user_id=None):
		user_list = get_object_or_404(User, username=user_id)
		detail_list = get_object_or_404(StudentDetail, user = user_list )
		template_name = 'user_profile.html'
		return render(request, template_name, {'user_list':user_list, 'detail_list':detail_list})

class EditProfile(UpdateView):
	'''
	'''
	model = StudentDetail
	form_class = StudentForm
	template_name = "edit_profile.html"

	#to ensure that a user can not edit someone else's profile
	# def get_object(self, queryset=None): 
	# 	return User.objects.get_or_create(user=self.request.user)[0]

	# def get_success_url(self):
	# 	return reverse("profile", kwargs={'slug': self.request.user})
