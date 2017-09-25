from django.contrib import admin
from .models import WifiDetail


class WifiAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'name', 'old_laptop_mac_address', 'new_laptop_mac_address', 'branch', 'mac_registered', 'created', 'modified')
    search_fields = ('old_laptop_mac_address', 'new_laptop_mac_address', 'user__username',)


admin.site.register(WifiDetail, WifiAdmin)
