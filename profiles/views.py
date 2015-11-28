from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse

from .models import StudentDetail, FacultyDetail
from .forms import StudentForm, FacultyForm
import permissions
# Create your views here.

class Home(View):
	'''
	'''
	def get(self,request):
		template_name = 'index.html'
		return render(request, template_name)

class UserProfile(LoginRequiredMixin, View):
	'''
	'''
	def get(self,request, user_id=None):
		user_type = None
		user_list = get_object_or_404(User, username=user_id)
		detail_list = None
		if permissions.is_in_group(user_list, 'StudentGroup'):
			user_type = 'student'
			detail_list = get_object_or_404(StudentDetail, user = user_list )
		elif permissions.is_in_group(user_list, 'FacultyGroup'):
			user_type = 'faculty'
			detail_list = get_object_or_404(FacultyDetail, user = user_list )
		template_name = 'user_profile.html'
		return render(request, template_name, {'user_type':user_type, 'user_list':user_list, 'detail_list':detail_list})

class EditProfile(LoginRequiredMixin, View):
	'''
	'''

	def get(self, request, slug=None):
		user = request.user 
		detail = None
		form = None
		if permissions.is_in_group(user, 'StudentGroup'):
			detail =  get_object_or_404(StudentDetail, pk=slug)
			form = StudentForm(instance=detail)
		elif permissions.is_in_group(user, 'FacultyGroup'):
			detail =  get_object_or_404(FacultyDetail, pk=slug)
			form = FacultyForm(instance=detail)
		template_name = "edit_profile.html"
		return render(request, template_name, {'form':form})

	def post(self, request, slug=None):
		user = request.user
		detail =  None
		form = None
		if permissions.is_in_group(user, 'StudentGroup'):
			detail =  get_object_or_404(StudentDetail, pk=slug)
			form = StudentForm(	request.POST,instance=detail)
		elif permissions.is_in_group(user, 'FacultyGroup'):
			detail =  get_object_or_404(FacultyDetail, pk=slug)
			form = FacultyForm(request.POST,instance=detail)
		template_name = 'user_profile.html'
		if form.is_valid():
			detail = form.save()	
		return redirect("user-profile", user_id= user.username)
