from django.contrib import admin
from .models import StudentDetail , FacultyDetail
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ('__unicode__','univ_roll_no','branch','year')

admin.site.register(StudentDetail, StudentAdmin)

class FacultyAdmin(admin.ModelAdmin):
	list_display = ('__unicode__','department','contact_no','alternate_email')
admin.site.register(FacultyDetail, FacultyAdmin)
