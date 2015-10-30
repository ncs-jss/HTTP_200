from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse

from .models import StudentDetail
from .forms import StudentForm

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
		user_list = get_object_or_404(User, username=user_id)
		detail_list = get_object_or_404(StudentDetail, user = user_list )
		template_name = 'user_profile.html'
		return render(request, template_name, {'user_list':user_list, 'detail_list':detail_list})

class EditProfile(LoginRequiredMixin, UpdateView):
	'''
	'''
	model = StudentDetail
	form_class = StudentForm
	template_name = "edit_profile.html"
	slug_field = 'user'
	
	def get_success_url(self):
		return reverse("user-profile", kwargs={'user_id': self.request.user.username})

	def get_object(self, *args, **kwargs):
		'''
		To verify that the user is permitted to visit the page for editing
		'''
		obj = super(EditProfile, self).get_object(*args, **kwargs)
		if not obj.user == self.request.user:
			raise PermissionDenied # maybe you'll need to write a middleware to catch 403's same way
		return obj
