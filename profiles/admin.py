from django.contrib import admin
from .models import StudentDetail, FacultyDetail, ContactUsMessage
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class StudentResource(resources.ModelResource):

    class Meta:
        model = StudentDetail


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('__unicode__', 'univ_roll_no', 'branch', 'year', 'section')
    resource_class = StudentResource
    pass


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'department', 'contact_no', 'alternate_email')

admin.site.register(FacultyDetail, FacultyAdmin)
admin.site.register(StudentDetail, StudentAdmin)
admin.site.register(ContactUsMessage)
