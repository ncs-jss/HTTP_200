from django.contrib import admin
from .models import StudentDetail, FacultyDetail, ContactMessage
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class StudentResource(resources.ModelResource):

    class Meta:
        model = StudentDetail


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('__unicode__', 'univ_roll_no', 'branch', 'year', 'section')
    search_fields = ('user__username',)
    resource_class = StudentResource
    pass


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'department', 'contact_no', 'alternate_email')
    search_fields = ('user__username',)


class ContactAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'email', 'message', 'message_sent')
	search_fields = ('name', 'email',)


admin.site.register(FacultyDetail, FacultyAdmin)
admin.site.register(StudentDetail, StudentAdmin)
admin.site.register(ContactMessage, ContactAdmin)
