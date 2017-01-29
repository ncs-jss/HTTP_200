from rest_framework import serializers
from rest_framework.serializers import (
    CharField,
    ValidationError,
)
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from profiles.models import FacultyDetail, StudentDetail


class UserLoginSerializer(serializers.ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    group = CharField(allow_blank=False, read_only=True)
    # This is the id of the user from the Student Profile or Faculty Profile table.
    user_id = CharField(allow_blank=False, read_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'password',
            'token',
            'group',
            'user_id',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user_obj = None
        username = data.get("username")
        password = data.get("password")
        if not username:
            raise ValidationError("A username is required.")

        user = User.objects.filter(
            Q(username=username)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This Username is not valid.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect Credentials.")

        token = Token.objects.get_or_create(user=user_obj)
        data["token"] = token[0]
        group = user_obj.groups.all()[0].name.lower()
        data["group"] = group
        data["first_name"] = user_obj.first_name

        if group == "student":
            data["user_id"] = StudentDetail.objects.filter(user=user)[0].id
        else:
            data["user_id"] = FacultyDetail.objects.filter(user=user)[0].id

        return data


class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentDetail
        fields = [
            'course',
            'branch',
            'year',
            'section',
            'univ_roll_no',
            'contact_no',
            'father_name',
            'mother_name',
            'address',
            'display_to_others',
        ]
