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
	univ_roll_no = models.PositiveIntegerField()
	ph_no = models.PositiveIntegerField()
	father_name = models.CharField(max_length = 200)
	mother_name = models.CharField(max_length = 200)
	address = models.CharField(max_length = 500)
	course = models.CharField(max_length = 3,
		choices = COURSE,
		default = BTech)
	bookmarks = JSONField()

class Faculty(models.Model):
	'''
	It stores the information about the faculties of college
	'''
	user = models.OneToOneField(User)
	designation = models.CharField(max_length = 100)
	department = models.CharField(max_length = 100)
	ph_no = models.PositiveIntegerField()
	address = models.CharField(max_length = 500)
	alternate_email = models.EmailField(max_length = 254)
	bookmarks = JSONField()

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
	owner = models.ForeignKey(User, related_name='notices', default = None)
	title = models.CharField(max_length = 500)
	description = models.TextField()
	details = JSONField()
	file_attached = models.FileField(upload_to = "attachments")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True,editable = True)
	category = models.CharField(max_length = 4,
		choices = CATEGORY,
		default = MISC)
	scheduled_time = models.DateTimeField(blank=True,auto_now_add=True)
