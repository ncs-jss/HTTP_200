from rest_framework import serializers
from message.models import Message, Notification

class NotificationSerializer(serializers.Serializer):
	seen = serializers.BooleanField()
	sent = serializers.BooleanField()
	seen_at = serializers.DateTimeField()

class MessageViewSerializer(serializers.ModelSerializer):
	notification = NotificationSerializer(many=True)
	sender = serializers.SerializerMethodField('return_sender')
	reciever = serializers.SerializerMethodField('return_reciever')
	
	def return_sender(self, obj):
		return obj.sender.username

	def return_reciever(self, obj):
		return obj.reciever.username

	class Meta:
		model = Message


