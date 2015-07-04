from django.forms import widgets
from rest_framework import serializers
from feeds.models import *

class StudentSerializer(serializers.ModelSerializer):
	'''
	Serializer Class for Student Model
	'''
	class Meta:
		model = Student
		fields = ('name','univ_roll_no','ph_no','father_name','mother_name','address', 'email_id','course','bookmarks')

	def create(self, validated_data):
		"""
		Create and return a new `Student` instance, given the validated data.
		"""
		return Student.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name',instance.name)
		# instance.user_id = validated_data.get('user_id',instance.user_id)
		instance.univ_roll_no = validated_data.get('univ_roll_no',instance.univ_roll_no)
		instance.ph_no = validated_data.get('ph_no',instance.ph_no)
		instance.father_name = validated_data.get('father_name',instance.father_name)
		instance.mother_name = validated_data.get('mother_name',instance.mother_name)
		instance.address = validated_data.get('address',instance.address)
		instance.email_id = validated_data.get('email_id',instance.email_id)
		instance.course = validated_data.get('course',instance.course)
		# instance.date_joined = validated_data.get('date_joined',instance.date_joined)
		instance.bookmarks = validated_data.get('bookmarks',instance.bookmarks)
		# instance.last_login = validated_data.get('last_login',instance.last_login)
		# instance.password_reset = validated_data.get('password_reset',instance.password_reset)
		instance.save()
		return instance


class FacultySerializer(serializers.ModelSerializer):
	'''
	Serializer Class for Faculty Model
	'''
	notice_uploaded = serializers.PrimaryKeyRelatedField(many=True, queryset=Notice.objects.all())
	class Meta:
		model = Faculty
		fields = ('notice_uploaded','name','designation','department','ph_no','address', 'email_id','alternate_email','bookmarks')

	def create(self, validated_data):
		"""
		Create and return a new `Faculty` instance, given the validated data.
		"""
		return Faculty.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name',instance.name)
		# instance.user_id = validated_data.get('user_id',instance.user_id)
		instance.designation = validated_data.get('designation',instance.designation)
		instance.department = validated_data.get('department',instance.department)
		# instance.date_joined = validated_data.get('date_joined',instance.date_joined)
		instance.ph_no = validated_data.get('ph_no',instance.ph_no)
		instance.address = validated_data.get('address',instance.address)
		instance.email_id = validated_data.get('email_id',instance.email_id)
		instance.alternate_email = validated_data.get('alternate_email',instance.alternate_email)
		instance.bookmarks = validated_data.get('bookmarks',instance.bookmarks)
		# instance.last_login = validated_data.get('last_login',instance.last_login)
		# instance.password_reset = validated_data.get('password_reset',instance.password_reset)
		instance.save()
		return instance


class NoticeSerializer(serializers.ModelSerializer):
	'''
	Serializer Class for Notices Model
	'''
	faculty_id = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Notice
		fields = ('scheduled_time','title','faculty_id','description','details','file_attached','created_at','updated_at', 'category')

	def create(self, validated_data):
		"""
		Create and return a new `Notices` instance, given the validated data.
		"""
		return Notice.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.scheduled_time = validated_data.get('scheduled_time',instance.scheduled_time)
		instance.title = validated_data.get('title',instance.title)
		instance.faculty_id = validated_data.get('faculty_id',instance.faculty_id)
		instance.description = validated_data.get('description',instance.description)
		instance.details = validated_data.get('details',instance.details)
		instance.file_attached = validated_data.get('file_attached',instance.file_attached)
		instance.created_at = validated_data.get('created_at',instance.created_at)
		instance.updated_at = validated_data.get('updated_at',instance.updated_at)
		instance.category = validated_data.get('category',instance.category)
		instance.save()
		return instance

# class ScheduledNoticeSerializer(serializers.ModelSerializer):
# 	'''
# 	Serializer Class for Scheduled Notices Model
# 	'''
# 	class Meta:
# 		model = ScheduledNotices
# 		fields = ('scheduled_time','title','faculty_id','description','details','file_attached','created_at','updated_at', 'category')

# 	def create(self, validated_data):
# 		"""
# 		Create and return a new `ScheduledNotices` instance, given the validated data.
# 		"""
# 		return User.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		instance.title = validated_data.get('title',instance.title)
# 		instance.faculty_id = validated_data.get('faculty_id',instance.faculty_id)
# 		instance.description = validated_data.get('description',instance.description)
# 		instance.details = validated_data.get('details',instance.details)
# 		instance.file_attached = validated_data.get('file_attached',instance.file_attached)
# 		instance.created_at = validated_data.get('created_at',instance.created_at)
# 		instance.updated_at = validated_data.get('updated_at',instance.updated_at)
# 		instance.category = validated_data.get('category',instance.category)
# 		instance.save()
# 		return instance

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	notices = serializers.StringRelatedField(many=True,)
	class Meta:
		model = User
		fields = ('id', 'username','notices')