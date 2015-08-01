from django.forms import widgets
from rest_framework import serializers
from feeds.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

	notices = serializers.HyperlinkedRelatedField(many=True, view_name='notice-detail', read_only=True)
	class Meta:
		model = User
		fields = ('notices', 'id', 'username', 'email','first_name', 'last_name',)

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Serializer Class for Student Model
	'''
	class Meta:
		model = Student
		fields = ('id', 'univ_roll_no','ph_no','father_name','mother_name','address', 'course','bookmarks')

	def create(self, validated_data):
		"""
		Create and return a new `Student` instance, given the validated data.
		"""
		return Student.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.univ_roll_no = validated_data.get('univ_roll_no',instance.univ_roll_no)
		instance.ph_no = validated_data.get('ph_no',instance.ph_no)
		instance.father_name = validated_data.get('father_name',instance.father_name)
		instance.mother_name = validated_data.get('mother_name',instance.mother_name)
		instance.address = validated_data.get('address',instance.address)
		instance.course = validated_data.get('course',instance.course)
		instance.bookmarks = validated_data.get('bookmarks',instance.bookmarks)
		instance.save()
		return instance


class FacultySerializer(serializers.HyperlinkedModelSerializer):
	'''
	Serializer Class for Faculty Model
	'''
	notice_uploaded = serializers.PrimaryKeyRelatedField(many=True, queryset=Notice.objects.all())
	class Meta:
		model = Faculty
		fields = ('id', 'notice_uploaded','designation','department','ph_no','address', 'alternate_email', 'bookmarks')

	def create(self, validated_data):
		"""
		Create and return a new `Faculty` instance, given the validated data.
		"""
		return Faculty.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.designation = validated_data.get('designation',instance.designation)
		instance.department = validated_data.get('department',instance.department)
		instance.ph_no = validated_data.get('ph_no',instance.ph_no)
		instance.address = validated_data.get('address',instance.address)
		instance.alternate_email = validated_data.get('alternate_email',instance.alternate_email)
		instance.bookmarks = validated_data.get('bookmarks',instance.bookmarks)
		instance.save()
		return instance


class NoticeSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Serializer Class for Notices Model
	'''
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Notice
		fields = ('id', 'scheduled_time','title','owner','description','details','file_attached','created_at','updated_at', 'category')

	def create(self, validated_data):
		"""
		Create and return a new `Notices` instance, given the validated data.
		"""
		return Notice.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.scheduled_time = validated_data.get('scheduled_time',instance.scheduled_time)
		instance.title = validated_data.get('title',instance.title)
		instance.description = validated_data.get('description',instance.description)
		instance.details = validated_data.get('details',instance.details)
		instance.file_attached = validated_data.get('file_attached',instance.file_attached)
		instance.created_at = validated_data.get('created_at',instance.created_at)
		instance.updated_at = validated_data.get('updated_at',instance.updated_at)
		instance.category = validated_data.get('category',instance.category)
		instance.save()
		return instance


class NoticeListSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Serializer Class for Listing the notices only(not the details) that are available in Model
	'''
	owner = serializers.ReadOnlyField(source='owner.username')
	attachment_flag = serializers.SerializerMethodField('check_for_attachment')

	def check_for_attachment(self, Notice):
		return Notice.file_attached != '' 
	
	class Meta:
		model = Notice
		fields = ('id', 'title', 'owner', 'details', 'attachment_flag', 'created_at', 'category')

	# def create(self, validated_data):
	# 	"""
	# 	Create and return a new `Notices` instance, given the validated data.
	# 	"""
	# 	return Notice.objects.create(**validated_data)

	# def update(self, instance, validated_data):
	# 	instance.title = validated_data.get('title',instance.title)
	# 	instance.created_at = validated_data.get('created_at',instance.created_at)
	# 	instance.updated_at = validated_data.get('updated_at',instance.updated_at)
	# 	instance.category = validated_data.get('category',instance.category)
	# 	instance.save()
	# 	return instance	
