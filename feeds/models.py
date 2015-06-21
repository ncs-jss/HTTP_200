from django.db import models
from django.core.validators import URLValidator
from jsonfield import JSONField
# Create your models here.

class Student(models.Model):
    '''
    It stores information about the Students of college.
    '''
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
    name = models.CharField(max_length = 200)
    user_id = models.CharField(max_length = 100)
    univ_roll_no = models.PositiveIntegerField()
    ph_no = models.PositiveIntegerField()
    father_name = models.CharField(max_length = 200)
    mother_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)
    email_id = models.EmailField(max_length = 254, unique = True)
    course = models.CharField(max_length = 3,
        choices = COURSE,
        default = BTech)
    date_joined = models.DateTimeField()
    bookmarks = JSONField()
    last_login = models.DateTimeField()
    password_reset = models.CharField(max_length = 300)

class Faculty(models.Model):
	'''
	It stores the information about the faculties of college
	'''
	name = models.CharField(max_length = 200)
	user_id = models.CharField(max_length = 100)
	designation = models.CharField(max_length = 100)
	department = models.CharField(max_length = 100)
	date_joined = models.DateTimeField()
	ph_no = models.PositiveIntegerField()
	address = models.CharField(max_length = 500)
	email_id = models.EmailField(max_length = 254, unique = True)
	alternate_email = models.EmailField(max_length = 254,default=None)
	bookmarks = JSONField()
	last_login = models.DateTimeField()
	password_reset = models.CharField(max_length = 300)

class Notice(models.Model):
	'''
	It stores the information about the Notices
	'''
	title = models.CharField(max_length = 500)
	description = models.TextField()
	faculty_id = models.ForeignKey(Faculty)
	details = JSONField()
	file_attached = JSONField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	category = models.CharField(max_length = 100)
	scheduled_time = models.DateTimeField(default=None,blank=True)