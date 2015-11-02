from django.db import models
from profiles.models import FacultyDetail
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.
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
	faculty = models.ForeignKey(FacultyDetail)
	title = models.CharField(max_length = 500)
	description = models.TextField()
	file_attached = models.FileField(upload_to = "attachments", blank = True, null = True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True, editable = True)
	subject = models.CharField(max_length = 200)
	category = models.CharField(max_length = 4,
		choices = CATEGORY,
		default = MISC)
	# scheduled_time = models.DateTimeField(blank=True,auto_now_add=True)
	def get_absolute_url(self):
		return reverse('notice-list', args=[self.pk])


class NoticeBranchYear(models.Model):
	"""
	It stores the information of branches and year related to the particular notice
	"""
	CSE = 'CSE'
	IT = 'IT'
	EE = 'EE'
	ECE = 'ECE'
	EEE = 'EEE'
	CE = 'CE'
	IC = 'IC'
	ME = 'ME'
	MT = 'MT'
	MCA = 'MCA'
	MBA = 'MBA'
	MTECH = 'MTECH'
	ALL = 'ALL'
	BRANCH = (
		(CSE, 'Computer Science and Engineering'),
		(IT, 'Information Technology'),
		(EE, 'Electrical Engineering'),
		(ECE, 'Electronics and Communication Engineering'),
		(EEE, 'Electrical and Electronics Engineering'),
		(CE, 'Civil Engineering'),
		(IC, 'Instrumentation and Control Engineering'),
		(ME, 'Mechanical Engineering'),
		(MT, 'Manufacturing Technology'),
		(MCA, 'Masters of Computer Applications'),
		(MBA, 'Master of Business Adminsitration  '),
		(MTECH, 'Masters of Technology'),
		(ALL, 'All branches and Courses')
		)
	notice = models.ForeignKey(Notice)
	year = models.PositiveIntegerField(default = 1)
	branch = models.CharField(
		max_length = 5,
		choices = BRANCH, 
		default = ALL,
		)

# apply AuthorPermissionLogic to Notice Model
# from permission import add_permission_logic
# from permission.logics import AuthorPermissionLogic
# add_permission_logic(Notice, AuthorPermissionLogic(
# 	field_name='faculty',
# ))
