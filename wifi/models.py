from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentwifiDetail(models.Model):
	'''
	It stores information about the wifi form of all the users.
	'''
	user = models.OneToOneField(User)
	hosteler = models.BooleanField()
	laptop_mac_address = models.CharField(max_length=200, blank=False, null=False)

	created = models.DateTimeField("Created", null=True, auto_now_add=True)
	modified = models.DateTimeField("Last Modified", null=True, auto_now=True)
	