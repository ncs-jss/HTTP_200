from rest_framework import serializers
from private_notices.models import PrivateNotice, Notification


class NotificationSerializer(serializers.Serializer):
    seen = serializers.BooleanField()
    sent = serializers.BooleanField()
    seen_at = serializers.DateTimeField()


class PrivateNoticeViewSerializer(serializers.ModelSerializer):
    pnotice = serializers.CharField(max_length=500)
    reciever = serializers.SerializerMethodField('return_reciever')
    sender = serializers.SerializerMethodField('return_sender')
    notification = NotificationSerializer(many=True)
            
    def return_sender(self, obj):
        return obj.sender.username

    def return_reciever(self, obj):
        return obj.reciever.username

    class Meta:
        model = PrivateNotice


class UserNotificationSerializer(serializers.ModelSerializer):
    pass
