from rest_framework import serializers

from notifications.models import FirebaseToken, NotificationPreference


class FirebaseTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = FirebaseToken
        fields = [
            'user_id',
            'firebase_token',
        ]


class NotificationPreferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificationPreference
        fields = [
            'user_id',
            'notification_preferences',
        ]
