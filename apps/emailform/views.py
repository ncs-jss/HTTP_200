from .models import EmailDetail
from profiles.models import StudentDetail
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.views.generic import View
from django.core.urlresolvers import reverse
from notices.decorators import student_profile_complete, default_password_change
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render
from .forms import EmailForm


class StudentEmailForm(LoginRequiredMixin, View):

    @method_decorator(default_password_change)
    @method_decorator(student_profile_complete)
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        details = StudentDetail.objects.get(user=user)
        try:
            email_data = EmailDetail.objects.get(user=user)
            if email_data:
                return render(request, 'email/studentemailform.html', {"user": user, "details": details, "email_data": email_data})
        except BaseException:
            return render(request, 'email/studentemailform.html', {"user": user, "details": details})

    def post(self, request):
        user = User.objects.get(username=request.user.username)

        try:
            email_data = EmailDetail.objects.get(user=user)
            email_form = EmailForm(request.POST, request.FILES, instance=email_data)
        except BaseException:
            email_form = EmailForm(request.POST, request.FILES)

        if email_form.is_valid():
            email_form = email_form.save(commit=False)
            email_form.user = user
            email_form.save()
            messages.success(request, "Successfully Registered for Email")
            return HttpResponseRedirect(reverse("relevent-notice-list"))
        else:
            print email_form.errors
            messages.error(request, "Enter Valid data in the form.")
            return HttpResponseRedirect(reverse("student-email"))
