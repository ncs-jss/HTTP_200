from .models import WifiDetail
from profiles.models import StudentDetail, FacultyDetail
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse
from notices.decorators import student_profile_complete, default_password_change
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .forms import WifiForm

import xlsxwriter


class StudentWifiForm(LoginRequiredMixin, View):

    @method_decorator(default_password_change)
    @method_decorator(student_profile_complete)
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        details = StudentDetail.objects.get(user=user)
        try:
            mac_address = WifiDetail.objects.get(user=user)
            if mac_address:
                return render(request, 'wifi/studentwifiform.html', {"user": user, "details": details, "mac_address": mac_address})
        except BaseException:
            return render(request, 'wifi/studentwifiform.html', {"user": user, "details": details})

    def post(self, request):
        user = User.objects.get(username=request.user.username)

        try:
            detail = WifiDetail.objects.get(user=user)
            wifi_form = WifiForm(request.POST, instance=detail)
        except BaseException:
            wifi_form = WifiForm(request.POST)

        if wifi_form.is_valid():
            wifi_form = wifi_form.save(commit=False)
            wifi_form.user = user
            wifi_form.save()
            messages.success(request, "Successfully Registered for Wi-Fi")
            return HttpResponseRedirect(reverse("relevent-notice-list"))
        else:
            # print wifi_form.errors
            messages.error(request, "Enter Mac Address in Given Format.")
            return HttpResponseRedirect(reverse("student-wifi"))


class FacultyWifiForm(LoginRequiredMixin, View):

    @method_decorator(default_password_change)
    @method_decorator(student_profile_complete)
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        details = FacultyDetail.objects.get(user=user)
        return render(request, 'wifi/facultywifiform.html', {"user": user, "details": details})

    def post(self, request):
        user = User.objects.get(username=request.user.username)
        profile = WifiDetail.objects.filter(user=user)
        if profile:
            messages.error(request, "Already Registered")
            return HttpResponseRedirect(reverse("relevent-notice-list"))
        else:
            user = User.objects.get(username=request.user.username)
            wifi_form = WifiForm(request.POST)
            if wifi_form.is_valid():
                wifi_form = wifi_form.save(commit=False)
                wifi_form.user = user
                wifi_form.save()
                messages.success(request, "Successfully Registered for Wi-Fi")
                return HttpResponseRedirect(reverse("relevent-notice-list"))
            else:
                messages.error(request, "Enter Laptop Mac Address")
                return HttpResponseRedirect(reverse("faculty-wifi"))


class excel_writer(LoginRequiredMixin, View):

    def get(self, request):
        '''
        Custom class to download Xls File .
        '''

        workbook = xlsxwriter.Workbook("wifi_details.xls")
        worksheet = workbook.add_worksheet()
        wifi = WifiDetail.objects.all()
        bold = workbook.add_format({'bold': True})
        worksheet.set_column(1, 160, 7)
        columns = ["Username", "First Name", "Last Name", "Course", "Branch", "Year", "Old_Laptop Mac Address", "New_Laptop_mac_address", "Date Applied"]
        row = 0
        for i, elem in enumerate(columns):
            worksheet.write(row, i, elem, bold)

        row += 1
        for users in wifi:
            # print users
            date_registered = str(users.created).split(' ')[0]
            try:
                user = User.objects.get(username=users.user)
                student = StudentDetail.objects.get(user=user)
                worksheet.write(row, 0, user.username)
                worksheet.write(row, 1, user.first_name)
                worksheet.write(row, 2, user.last_name)
                worksheet.write(row, 3, student.course)
                worksheet.write(row, 4, student.branch)
                worksheet.write(row, 5, student.year)
                worksheet.write(row, 6, users.old_laptop_mac_address)
                worksheet.write(row, 7, users.new_laptop_mac_address)
                worksheet.write(row, 8, date_registered)
                row += 1
            except BaseException:
                user = User.objects.get(username=users.user)
                faculty = FacultyDetail.objects.get(user=user)
                worksheet.write(row, 0, user.username)
                worksheet.write(row, 1, user.first_name)
                worksheet.write(row, 2, user.last_name)
                worksheet.write(row, 4, faculty.department)
                worksheet.write(row, 6, users.old_laptop_mac_address)
                worksheet.write(row, 7, users.new_laptop_mac_address)
                worksheet.write(row, 8, date_registered)
                row += 1

        workbook.close()
        response = HttpResponse(file("wifi_details.xls"))
        response['Content-Type'] = "application/vnd.ms-excel"
        response['Content-Disposition'] = 'attachment; filename="wifi_details.xls"'
        return response
