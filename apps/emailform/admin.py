from django.contrib import admin
from .models import EmailDetail


class EmailAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'name', 'hod_approval', 'created', 'modified')
    search_fields = ('email', 'name', 'email_purpose')
    list_filter = ('hod_approval',)


admin.site.register(EmailDetail, EmailAdmin)
