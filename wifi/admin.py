from django.contrib import admin
from .models import WifiDetail


class WifiAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'name', 'laptop_mac_address', 'branch', 'mac_registered',)
    search_fields = ('laptop_mac_address', 'user',)

admin.site.register(WifiDetail, WifiAdmin)
