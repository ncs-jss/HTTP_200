from rest_framework import serializers

from notifications.models import FirebaseToken


class FirebaseTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = FirebaseToken
        fields = [
            'user_id',
            'firebase_token',
        ]
