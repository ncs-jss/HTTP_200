from django.contrib import admin
from message.models import Message, Notification

class NotificationInline(admin.StackedInline):
	model = Notification
	extra=1
	fields = ['mid','sent','seen','seen_at']

	
class MessageAdmin(admin.ModelAdmin):
	inlines = [NotificationInline,]
	list_display = ('sender', 'reciever', 'message','created_at', 'seen_yet')

	def seen_yet(self,obj):
		return obj.notification_set.get(mid=obj).seen

admin.site.register(Message, MessageAdmin)
