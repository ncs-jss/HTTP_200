from django.contrib import admin

from .models import FirebaseToken, Preferences


@admin.register(FirebaseToken)
class FirebaseTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "firebase_token",)
    list_filter = ("user",)
    search_fields = ("user",)


@admin.register(Preferences)
class Preferences(admin.ModelAdmin):
    list_display = ("user", "notification_preferences",)
    list_filter = ("user",)
    search_fields = ("user",)
