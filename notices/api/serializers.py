from rest_framework import serializers
from notices.models import Notice 

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    SerializerMethodField,
    )


class NoticeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = [
        'faculty',
        'title',
        'description',
        'file_attached',
        'category',
    ]


"""
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjE3Y3NlMDAxIiwidXNlcl9pZCI6MTMsImVtYWlsIjoiIiwiZXhwIjoxNDc3MTY0MzI0fQ.OxqVAI6fzT33ccx9qSccVAwGzzeaPdNDUdMaFBuodmM

curl -X POST -d eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjE3Y3NlMDAxIiwidXNlcl9pZCI6MTMsImVtYWlsIjoiIiwiZXhwIjoxNDc3MTY0MzI0fQ.OxqVAI6fzT33ccx9qSccVAwGzzeaPdNDUdMaFBuodmM http://127.0.0.1:8000/api/notices/

"""
