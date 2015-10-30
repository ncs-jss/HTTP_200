from django.db import models
from django.core.validators import URLValidator
from django.core import urlresolvers
from jsonfield import JSONField
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class StudentDetail(models.Model):
	'''
	It stores information about the Students of college.
	'''
	user = models.OneToOneField(User)
	BTech = 'BT'
	MCA = 'MCA'
	MBA = 'MBA'
	OTHERS = 'OT'
	COURSE = (
		(BTech, 'B.Tech'),
		(MCA,'MCA'),
		(MBA,'MBA'),
		(OTHERS,'Others'),
		)
	univ_roll_no = models.PositiveIntegerField()
	contact_no = models.PositiveIntegerField(null = True,editable = True)
	father_name = models.CharField(max_length = 200, null = True)
	mother_name = models.CharField(max_length = 200, null = True)
	address = models.CharField(max_length = 500, null = True,editable = True)
	course = models.CharField(max_length = 3,
		choices = COURSE,
		default = BTech)
	display_to_others = models.BooleanField(default=True)
	# relevent_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# academics_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# administration_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# misc_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# tnp_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# events_last_seen = models.DateTimeField(auto_now_add=True,editable = True)

	def __unicode__(self):
		return self.user.username + " details"

	@property
	def get_edit_url(self):
		edit_url = "/user/"+self.user.username+"/edit"
		return edit_url

class FacultyDetail(models.Model):
	'''
	It stores the information about the faculties of college
	'''
	user = models.OneToOneField(User)
	designation = models.CharField(max_length = 100, null = True,editable = True)
	department = models.CharField(max_length = 100, null = True,editable = True)
	contact_no = models.PositiveIntegerField(null = True,editable = True)
	address = models.CharField(max_length = 500, null = True,editable = True)
	alternate_email = models.EmailField(max_length = 254, null = True,editable = True)
	display_to_others = models.BooleanField(default=True)
	# relevent_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# academics_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# administration_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# misc_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# tnp_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	# events_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
