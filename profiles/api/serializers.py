#Django Imports
from django.contrib.auth import get_user_model

# Rest Framework Imports
from rest_framework import serializers
from rest_framework.serializers import (
	CharField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError,
	)

from django.contrib.auth.models import Group, User
from django.db.models import Q
from rest_framework.authtoken.models import Token


class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField()
	class Meta:
		model = User
		fields = [
		'username',
		'password',
		'token',
		]
		extra_kwargs = { "password" :
						{"write_only" : True }
						}

	def validate(self, data):
		user_obj = None
		username = data.get("username")
		password = data.get("password")
		if not username:
			raise ValidationError("A username is required.")

		user = User.objects.filter(
			Q(username=username)
			).distinct()
		print "I am the user",user
		if user.exists() and user.count() == 1:
			user_obj = user.first()
		else:
			raise ValidationError("This Username is not valid.")
		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("Incorrect Credentials.")

		token = Token.objects.create(user=user_obj)
		data["token"] = token
		print token.key

		return data





