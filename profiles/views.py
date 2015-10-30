from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

from .models import StudentDetail

# Create your views here.
class UserProfile(View):
	def get(self,request, user_id=None):
		user_list = get_object_or_404(User, username=user_id)
		detail_list = get_object_or_404(StudentDetail, user = user_list )
		template_name = 'user_profile.html'
		return render(request, template_name, {'user_list':user_list, 'detail_list':detail_list})

class Home(View):
	def get(self,request):
		template_name = 'index.html'
		return render(request, template_name)
