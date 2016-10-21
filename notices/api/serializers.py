from rest_framework import serializers
from notices.models import Notice

from rest_framework.serializers import (
    SerializerMethodField,
    CharField,
)
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class NoticeListSerializer(serializers.ModelSerializer):
    faculty = SerializerMethodField()
    token = CharField()

    class Meta:
        model = Notice
        fields = [
            'faculty',
            'title',
            'description',
            'file_attached',
            'category',
            'created',
            'modified',
        ]

    def get_faculty(self, obj):

        return str(obj.faculty.user.first_name)

    def get_file_attached(self, obj):
        try:
            file_attached = obj.file_attached.url
            APP_DIR = "http://127.0.0.1:8000/media/"
            return APP_DIR + str(file_attached)
        except:
            file_attached = None

        return file_attached

    def validate(self, request):
        token = request.META.get('Authorization')
        username = request.META.get('username')

        if not username:
            raise validationError("A username is required.")

        user = User.objects.filter(
            Q(username=username)
        ).distinct()

        token_obj = Token.objects.filter(
            Q(username=username)
        ).distinct()

        if user.exists() and token == token_obj:
            print "user is authenticated."

        
