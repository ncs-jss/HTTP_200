from django.contrib.auth.models import User
from profiles.models import StudentDetail, FacultyDetail, ContactMessage
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import check_password


def student_profile_complete(function):
	"""
	Decorator to check that user profile is completed or not.
	"""
	def _inner(request, *args, **kwargs):
		user = User.objects.get(username=request.user.username)
		profile = StudentDetail.objects.get(user=user)
		if user.first_name and user.last_name and user.email and profile.course and profile.branch and profile.year and profile.contact_no and profile.address and profile.mother_name and profile.father_name:
			print "enter if "
			return HttpResponseRedirect(reverse("relevent-notice-list"))			
		else:
			print "enter else"
			return HttpResponseRedirect(reverse("user-profile", kwargs={"user_id": str(request.user.username)}))
	return _inner


def student_password_change(function):
	"""
	Decorator to check if user password is changed or not.
	"""
	def _password(request, *args, **kwargs):
		user = User.objects.get(username=request.user.username)
		if check_password(str(request.user.username), user.password):
			return HttpResponseRedirect(reverse("password_change"))
		else:
			return HttpResponseRedirect(reverse("user-profile", kwargs={"user_id": str(request.user.username)}))
	return _password



