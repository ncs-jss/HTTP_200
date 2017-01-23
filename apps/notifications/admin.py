from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
	list_display = ("user", "firebase_token", "notification_preference")
	list_filter = ("user",)
	search_fields = ("user",)
