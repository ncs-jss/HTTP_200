from django.contrib.auth import get_user_model

from rest_framework import serializers

from notices.models import Notice
from profiles.models import FacultyDetail

User = get_user_model()


class NoticeListSerializer(serializers.ModelSerializer):
    faculty = serializers.SerializerMethodField()
    file_attached = serializers.SerializerMethodField()
    notice_id = serializers.SerializerMethodField()

    class Meta:
        model = Notice
        fields = (
            'notice_id',
            'faculty',
            'title',
            'description',
            'file_attached',
            'category',
            'created',
            'modified',
        )

    def get_faculty(self, obj):

        return str(obj.faculty.user.first_name)

    def get_file_attached(self, obj):
        try:
            file_attached = obj.file_attached.url
        except:
            file_attached = None

        return file_attached

    def get_notice_id(self, obj):

        return str(obj.id)


class NoticeCreateSerializer(serializers.ModelSerializer):
    faculty = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=FacultyDetail.objects.all(),
    )

    class Meta:
        model = Notice
        fields = [
            'faculty',
            'title',
            'description',
            'file_attached',
            'category',
            'visible_for_student',
            'visible_for_hod',
            'visible_for_faculty',
            'visible_for_management',
            'visible_for_others',
            'course_branch_year',
            'created',
            'modified',
        ]
