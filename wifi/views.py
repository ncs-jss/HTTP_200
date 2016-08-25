from django.shortcuts import render
from .models import StudentwifiDetail
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.views.generic import View
from django.core.urlresolvers import reverse


class WifiForm(LoginRequiredMixin, View):
	
	def get(self, request):
		return render(request, 'wifi/wifiform.html')

	def post(self, request):
		hosteler = request.POST.get("hosteler")
		laptop_mac_address = request.POST.get("laptop_mac_address")
		user = User.objects.get(username=request.user.username)
		profile = StudentwifiDetail.objects.filter(user=user)
		if profile:
			return render(request, 'wifi/wifiform.html', {"error":"you have already applied for it."})
		else:
			StudentwifiDetail.objects.create(user=user, hosteler=hosteler, laptop_mac_address=laptop_mac_address)
			return HttpResponseRedirect(reverse("relevent-notice-list"))