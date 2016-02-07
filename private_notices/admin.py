from django.contrib import admin
from private_notices.models import PrivateNotice, Notification


class NotificationInline(admin.StackedInline):
    model = Notification
    extra = 1
    fields = ['mid', 'sent', 'seen', 'seen_at']


class PrivateNoticeAdmin(admin.ModelAdmin):
    inlines = [NotificationInline, ]
    list_display = ('sender', 'reciever', 'pnotice', 'created_at', 'seen_yet')

    def seen_yet(self, obj):
        return obj.notification.get(mid=obj).seen

admin.site.register(PrivateNotice, PrivateNoticeAdmin)
