from django.shortcuts import render
from .models import WifiDetail
from profiles.models import StudentDetail, FacultyDetail
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.views.generic import View
from django.core.urlresolvers import reverse
from notices.decorators import student_profile_complete, default_password_change
from django.utils.decorators import method_decorator


class StudentWifiForm(LoginRequiredMixin, View):

	@method_decorator(default_password_change)
	@method_decorator(student_profile_complete)
	def get(self, request):
		user = User.objects.get(username=request.user.username)
		details = StudentDetail.objects.get(user=user)
		return render(request, 'wifi/studentwifiform.html', {"user": user, "details": details})

	def post(self, request):
		hosteler = request.POST.get("hosteler")
		laptop_mac_address = request.POST.get("laptop_mac_address")
		user = User.objects.get(username=request.user.username)
		profile = WifiDetail.objects.filter(user=user)
		if profile:
			return render(request, 'wifi/studentwifiform.html', {"error": "you have already applied for it.", "user": user, "details": details})
		else:
			WifiDetail.objects.create(user=user, hosteler=hosteler, laptop_mac_address=laptop_mac_address)
			return HttpResponseRedirect(reverse("relevent-notice-list"))


class FacultyWifiForm(LoginRequiredMixin, View):

	@method_decorator(default_password_change)
	@method_decorator(student_profile_complete)
	def get(self, request):
		user = User.objects.get(username=request.user.username)
		details = FacultyDetail.objects.get(user=user)
		return render(request, 'wifi/facultywifiform.html', {"user": user, "details": details})

	def post(self, request):
		laptop_mac_address = request.POST.get("laptop_mac_address")
		user = User.objects.get(username=request.user.username)
		details = FacultyDetail.objects.get(user=user)
		profile = WifiDetail.objects.filter(user=user)
		if profile:
			return render(request, 'wifi/facultywifiform.html', {"error": "You have already applied for it.", "user": user, "details": details})
		else:
			WifiDetail.objects.create(user=user, laptop_mac_address=laptop_mac_address)
			return HttpResponseRedirect(reverse("relevent-notice-list"))
