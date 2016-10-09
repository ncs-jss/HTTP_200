from rest_framework import serializers
from notices.models import Notice 

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    SerializerMethodField,
    )


class NoticeListSerializer(serializers.ModelSerializer):
    faculty = SerializerMethodField()
    file_attached = SerializerMethodField()
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


"""
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjE3Y3NlMDAxIiwidXNlcl9pZCI6MTMsImVtYWlsIjoiIiwiZXhwIjoxNDc3MTY0MzI0fQ.OxqVAI6fzT33ccx9qSccVAwGzzeaPdNDUdMaFBuodmM

curl -X GET -d eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjE3Y3NlMDAxIiwidXNlcl9pZCI6MTMsImVtYWlsIjoiIiwiZXhwIjoxNDc3Mjk5OTUzfQ.tUPex3QSHI_G57rbY5t8w1DGp4SOa61fzJHIyCbGAu4 'http://127.0.0.1:8000/api/notices/'


curl -X POST -d "username=17cse001&password=17cse001" http://127.0.0.1:8000/api/auth/token/
"""
