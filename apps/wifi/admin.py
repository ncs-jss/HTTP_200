from django.contrib import admin
from .models import WifiDetail, EmailDetail


class WifiAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'name', 'old_laptop_mac_address', 'new_laptop_mac_address', 'branch', 'mac_registered', 'created', 'modified')
    search_fields = ('old_laptop_mac_address', 'new_laptop_mac_address', 'user__username',)


class EmailAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'name', 'hod_approved_email', 'created', 'modified')
    search_fields = ('email', 'name', 'email_purpose')
    list_filter = ('hod_approved_email',)


admin.site.register(WifiDetail, WifiAdmin)
admin.site.register(EmailDetail, EmailAdmin)
