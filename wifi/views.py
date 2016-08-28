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
from django.contrib import messages


class StudentWifiForm(LoginRequiredMixin, View):

    @method_decorator(default_password_change)
    @method_decorator(student_profile_complete)
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        details = StudentDetail.objects.get(user=user)
        return render(request, 'wifi/studentwifiform1.html', {"user": user, "details": details})

    def post(self, request):
        hosteler = request.POST.get("hosteler")
        laptop_mac_address = request.POST.get("laptop_mac_address")
        user = User.objects.get(username=request.user.username)
        details = StudentDetail.objects.get(user=user)
        profile = WifiDetail.objects.filter(user=user)
        if profile:
            messages.error(request, "Already Registered")
            return HttpResponseRedirect(reverse("relevent-notice-list"))

        else:
            WifiDetail.objects.create(user=user, laptop_mac_address=laptop_mac_address)
            messages.success(request, "Successfully Registered for Wi-Fi")
            return HttpResponseRedirect(reverse("relevent-notice-list"))


class FacultyWifiForm(LoginRequiredMixin, View):

    @method_decorator(default_password_change)
    @method_decorator(student_profile_complete)
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        details = FacultyDetail.objects.get(user=user)
        return render(request, 'wifi/facultywifiform1.html', {"user": user, "details": details})

    def post(self, request):
        laptop_mac_address = request.POST.get("laptop_mac_address")
        user = User.objects.get(username=request.user.username)
        details = FacultyDetail.objects.get(user=user)
        profile = WifiDetail.objects.filter(user=user)
        if profile:
            messages.error(request, "Already Registered")
            return HttpResponseRedirect(reverse("relevent-notice-list"))
        else:
            WifiDetail.objects.create(user=user, laptop_mac_address=laptop_mac_address)
            messages.success(request, "Successfully Registered for Wi-Fi")
            return HttpResponseRedirect(reverse("relevent-notice-list"))


# def export_xls(modeladmin, request, queryset):
#     import xlwt
#     response = HttpResponse(mimetype='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=wifiregister.xls'
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet("WiFi-Register")

#     row_num = 0

#     columns = [
#     (u"ID", 5000),
#     (u"Laptop Mac Address", 5000),
#     ]

#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     for col_num in xrange(len(columns)):
#         ws.write(row_num, col_num, columns[col_num][0], font_style)
#         ws.col(col_num).width = columns[col_num][1]

#     font_style = xlwt.XFStyle()
#     font_style.alignment.wrap = 1

#     for obj in queryset:
#         row_num += 1
#         row = [
#                 obj.pk,
#                 obj.laptop_mac_address,
#         ]
#         for col_num in xrange(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)

#     wb.save(response)
#     return response

# export_xls.short_description = u"Export XLS"
