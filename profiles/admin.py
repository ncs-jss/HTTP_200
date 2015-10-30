from django.contrib import admin
from .models import StudentDetail , FacultyDetail
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	pass
admin.site.register(StudentDetail, StudentAdmin)

class FacultyAdmin(admin.ModelAdmin):
	pass
admin.site.register(FacultyDetail, FacultyAdmin)
