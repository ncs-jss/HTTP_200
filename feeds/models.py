from django.db import models
from django.core.validators import URLValidator
from jsonfield import JSONField
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
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
	name = models.CharField(max_length = 200,default = True)
	# user_id = models.CharField(max_length = 100)
	univ_roll_no = models.PositiveIntegerField()
	ph_no = models.PositiveIntegerField()
	father_name = models.CharField(max_length = 200)
	mother_name = models.CharField(max_length = 200)
	address = models.CharField(max_length = 500)
	# email_id = models.EmailField(max_length = 254, unique = True)
	course = models.CharField(max_length = 3,
		choices = COURSE,
		default = BTech)
	# date_joined = models.DateTimeField(default=datetime.now, blank=True)
	bookmarks = JSONField()
	# last_login = models.DateTimeField(default=datetime.now, blank=True)

class Faculty(models.Model):
	'''
	It stores the information about the faculties of college
	'''
	user = models.OneToOneField(User,default = True)
	name = models.CharField(max_length = 200, blank = True)
	# user_id = models.CharField(max_length = 100, blank = True)
	designation = models.CharField(max_length = 100)
	department = models.CharField(max_length = 100)
	# date_joined = models.DateTimeField()
	ph_no = models.PositiveIntegerField()
	address = models.CharField(max_length = 500)
	# email_id = models.EmailField(max_length = 254, unique = True, default=None)
	alternate_email = models.EmailField(max_length = 254,default=None)
	bookmarks = JSONField()
	# date_joined = models.DateTimeField(default=datetime.now, blank=True)
	# last_login = models.DateTimeField(default=datetime.now, blank=True)

class Notice(models.Model):
	'''
	It stores the information about the Notices
	'''
	ACADEMICS = 'ACD'
	ADMINISTRATION = 'ADMN'
	TNP = 'TNP'
	EVENTS = 'EVNT'
	MISC = 'MISC'
	CATEGORY = (
		(ACADEMICS, 'Academics'),
		(ADMINISTRATION,'Adminsitration'),
		(TNP,'Training and Placement'),
		(EVENTS,'Events'),
		(MISC,'Miscelleneous'),
		)
	title = models.CharField(max_length = 500)
	description = models.TextField()
	faculty_id = models.ForeignKey(Faculty)
	details = JSONField()
	file_attached = JSONField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	category = models.CharField(max_length = 4,
		choices = CATEGORY,
		default = MISC)
	scheduled_time = models.DateTimeField(default=datetime.now, blank=True)
