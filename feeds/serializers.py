from django.forms import widgets
from rest_framework import serializers
from feeds.models import *
from django.contrib.auth.models import User
from django.http import request

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ( 'id', 'username', 'email','first_name', 'last_name', 'last_login')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Serializer Class for Student Model
	'''
	user_fields = UserSerializer(source = 'user')
	relevent_count = serializers.ReadOnlyField(source='relevent')
	academics_count = serializers.ReadOnlyField(source='academics')
	administration_count = serializers.ReadOnlyField(source='administration')
	misc_count = serializers.ReadOnlyField(source='misc')
	tnp_count = serializers.ReadOnlyField(source='tnp')
	events_count = serializers.ReadOnlyField(source='events')

	class Meta:
		model = Student
		fields = ( 'user_fields', 'id', 'univ_roll_no','ph_no','father_name','mother_name','address', 'course', 'relevent_count', 'academics_count', 'administration_count', 'tnp_count', 'events_count', 'misc_count')

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
		instance.relevent_count = validated_data.get('relevent_count',instance.relevent_count)
		instance.academics_count = validated_data.get('academics_count',instance.academics_count)
		instance.administration_count = validated_data.get('administration_count',instance.administration_count)
		instance.tnp_count = validated_data.get('tnp_count',instance.tnp_count)
		instance.events_count = validated_data.get('events_count',instance.events_count)
		instance.misc_count = validated_data.get('misc_count',instance.misc_count)
		instance.save()
		return instance


class FacultySerializer(serializers.HyperlinkedModelSerializer):
	'''
	Serializer Class for Faculty Model
	'''
	user_fields = UserSerializer(source = 'user')
	relevent_count = serializers.ReadOnlyField(source='relevent')
	academics_count = serializers.ReadOnlyField(source='academics')
	administration_count = serializers.ReadOnlyField(source='administration')
	misc_count = serializers.ReadOnlyField(source='misc')
	tnp_count = serializers.ReadOnlyField(source='tnp')
	events_count = serializers.ReadOnlyField(source='events')
	# notice_uploaded = serializers.PrimaryKeyRelatedField(many=True, queryset=Notice.objects.all())
	notices = serializers.HyperlinkedRelatedField(many=True, view_name='notice-detail', read_only=True)
	class Meta:
		model = Faculty
		fields = ('user_fields', 'notices', 'id','designation','department','ph_no','address', 'alternate_email','relevent_count', 'academics_count', 'administration_count', 'tnp_count', 'events_count', 'misc_count')

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
		instance.relevent_count = validated_data.get('relevent_count',instance.relevent_count)
		instance.academics_count = validated_data.get('academics_count',instance.academics_count)
		instance.administration_count = validated_data.get('administration_count',instance.administration_count)
		instance.tnp_count = validated_data.get('tnp_count',instance.tnp_count)
		instance.events_count = validated_data.get('events_count',instance.events_count)
		instance.misc_count = validated_data.get('misc_count',instance.misc_count)
		instance.save()
		return instance


class NoticeSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Serializer Class for Notices Model
	'''
	owner = serializers.ReadOnlyField(source='owner.username')
	# currenet_user = serializers.SerializerMethodField(source = 'check_for_current_user')
	# bookmark_flag = SerializerMethodField(source = 'check_for_bookmark')
	# def check_for_bookmark(self, BookmarkedNotice):
	# def check_for_current_user(self, )
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
	bookmark_flag = serializers.SerializerMethodField('check_for_bookmark')
	
	def check_for_bookmark(self, Notice):
		if BookmarkedNotice.objects.filter(notice = Notice.id ).count()==1:
			return True
		else:
			return False

	def check_for_attachment(self, Notice):
		return Notice.file_attached != '' 
	
	class Meta:
		model = Notice
		fields = ('bookmark_flag', 'id', 'title', 'owner', 'details', 'attachment_flag', 'created_at', 'category')


class BookmarkSerializer(serializers.ModelSerializer):
	'''
	Serializer class for Bookmarks Model
	'''
	user = serializers.ReadOnlyField(source='user.username')
	class Meta:
		model = BookmarkedNotice
		fields = ('id','user', 'notice')

	def create(self, validated_data):
		"""
		Create and return a new `BookmarkedNotice` instance, given the validated data.
		"""
		return BookmarkedNotice.objects.create( **validated_data)

	def update(self, instance, validated_data):
		instance.id = validated_data.get('id',instance.id)
		instance.user = validated_data.get('user',instance.user)
		instance.notice = validated_data.get('notice',instance.notice)
		instance.save()
		return instance	
