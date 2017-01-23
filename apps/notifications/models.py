from django.contrib.auth.models import User
from django.db import models


class Notification(models.Model):
	"""
	It stores the firebase id with corresponding users and their preferences.
	"""
	user = models.OneToOneField(User)
	firebase_token = models.CharField(max_length=200, blank=False, null=False)
	notification_preference = models.CharField(max_length=200, blank=False, default='00000', null=False)
