from django.db import models
from django.core.validators import URLValidator
from jsonfield import JSONField
# Create your models here.

class Stuend(models.Model):
    '''
    It stores information about the Students of college.
    '''
    name = models.CharField(max_length = 200)
    user_id = models.CharField(max_length = 100)
    univ_roll_no = models.PositiveIntegerField()
    ph_no = models.PositiveIntegerField()
    father_name = models.CharField(max_length = 200)
    mother_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)
    email_id = models.EmailField(max_length = 254, unique = True)
    course = models.CharField(max_length 50)
    date_joined = models.DateTimeField()
    bookmarks = JSONField()
    last_login = models.DateTimeField()
    password_reset = models.CharField(max_length = 300)

class Faculty(models.Model)
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
	email = models.EmailField(max_length = 254, unique = True)
	bookmarks = JSONField()
	last_login = models.DateTimeField()
	password_reset = models.CharField(max_length = 300)

class Notices(models.Model)
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
	scheduled_time = models.DateTimeField()