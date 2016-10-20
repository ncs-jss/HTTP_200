from rest_framework import serializers
from notices.models import Notice

from rest_framework.serializers import (
    SerializerMethodField,
)


class NoticeListSerializer(serializers.ModelSerializer):
    faculty = SerializerMethodField()
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

