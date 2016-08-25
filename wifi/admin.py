from django.contrib import admin
from .models import StudentwifiDetail
# Register your models here.

class wifiAdmin(admin.ModelAdmin):
	search_fields = ('laptop_mac_address',)

admin.site.register(StudentwifiDetail, wifiAdmin)