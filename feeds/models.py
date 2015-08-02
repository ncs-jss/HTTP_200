from django.db import models
from django.core.validators import URLValidator
from django.core import urlresolvers
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
	ph_no = models.PositiveIntegerField(null = True)
	father_name = models.CharField(max_length = 200, null = True)
	mother_name = models.CharField(max_length = 200, null = True)
	address = models.CharField(max_length = 500, null = True)
	relevent_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	academics_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	administration_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	misc_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	tnp_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	events_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	course = models.CharField(max_length = 3,
		choices = COURSE,
		default = BTech)

	@property
	def relevent(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'Relevent').count()
		return count

	@property
	def administration(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'ADMN').count()
		return count

	@property
	def academics(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'ACD').count()
		return count

	@property
	def tnp(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'TNP').count()
		return count

	@property
	def events(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'EVNT').count()
		return count

	@property
	def misc(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'MISC').count()
		return count



class Faculty(models.Model):
	'''
	It stores the information about the faculties of college
	'''
	user = models.OneToOneField(User)
	designation = models.CharField(max_length = 100, null = True)
	department = models.CharField(max_length = 100, null = True)
	ph_no = models.PositiveIntegerField(null = True)
	address = models.CharField(max_length = 500, null = True)
	alternate_email = models.EmailField(max_length = 254, null = True)
	relevent_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	academics_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	administration_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	misc_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	tnp_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	events_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
	@property
	def relevent(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'Relevent').count()
		return count

	@property
	def administration(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'ADMN').count()
		return count

	@property
	def academics(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'ACD').count()
		return count

	@property
	def tnp(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'TNP').count()
		return count

	@property
	def events(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'EVNT').count()
		return count

	@property
	def misc(self):
		count = Notice.objects.filter(created_at__gt = self.last_login, category = 'MISC').count()
		return count

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
	owner = models.ForeignKey(Faculty, related_name='notices', default = None)
	title = models.CharField(max_length = 500)
	description = models.TextField()
	details = JSONField()
	file_attached = models.FileField(upload_to = "attachments", blank = True, null = True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True,editable = True)
	subject = models.CharField(max_length = 200)
	category = models.CharField(max_length = 4,
		choices = CATEGORY,
		default = MISC)
	scheduled_time = models.DateTimeField(blank=True,auto_now_add=True)

	def get_absolute_url(self):
		return urlresolvers.reverse('notice-detail', args=[self.pk])


class BookmarkedNotice(models.Model):
	"""
		Defines the databse table for storing the bookmarks as done by the user. 
	"""
	user = models.ForeignKey(User)
	notice = models.ForeignKey(Notice)
