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


"""

curl -X GET -d eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjE3Y3NlMDAxIiwidXNlcl9pZCI6MTMsImVtYWlsIjoiYWJjQHN3Zi5jb20iLCJleHAiOjE0Nzc0ODMyMTR9.l2y3iaZZVFsu7MHAYC94yuXPTuZdvFl_k_3uqsemqo4 'http://127.0.0.1:8000/api/notices/'

curl -X GET "username=17cse001&password=123" 'http://127.0.0.1:8000/api/notices/'

curl -X POST -d "username=17cse001&password=123" http://127.0.0.1:8000/api/auth/token/

"""

from django.contrib.auth.models import Group, User

class GroupSerializer(serializers.ModelSerializer):
    name = SerializerMethodField()
    class Meta:
        model = Group
        fields = [
        'name',
        ]


class UserSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True)
    model = User
    fields = [
    'group'
    ]
