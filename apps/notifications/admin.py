from django.contrib import admin

from .models import FirebaseToken, NotificationPreferences


@admin.register(FirebaseToken)
class FirebaseTokenAdmin(admin.ModelAdmin):
    list_display = ("user_id", "firebase_token",)
    list_filter = ("user_id",)
    search_fields = ("user_id",)


@admin.register(NotificationPreferences)
class NotificationPreferencesAdmin(admin.ModelAdmin):
    list_display = ("user_id", "notification_preferences",)
    list_filter = ("user_id",)
    search_fields = ("user_id",)
