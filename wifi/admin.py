from django.contrib import admin
from .models import WifiDetail


class WifiAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'laptop_mac_address', 'user_email', 'user_name')
	search_fields = ('laptop_mac_address', 'user',)

admin.site.register(WifiDetail, WifiAdmin)
