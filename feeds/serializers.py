from django.forms import widgets
from rest_framework import serializers
from feeds.models import *
from django.contrib.auth.models import User
from django.http import request

class UserSerializer(serializers.ModelSerializer):
	username = serializers.ReadOnlyField()
	password = serializers.CharField(style = {'input_type': 'password'}, default = 'password')

	class Meta:
		model = User
		fields = ( 'id', 'username', 'email', 'password', 'first_name', 'last_name', 'last_login')
	
	def create(self, validated_data):
		"""
		Create and return a new `Student` instance, given the validated data.
		"""
		user = User(email=validated_data['email'], username=validated_data['username'], first_name = validated_data['first_name'], last_name = validated_data['last_name'])
		user.set_password(validated_data['password'])
		user.save()
		return user

	def update(self, instance, validated_data):
		print validated_data
		instance.username = validated_data.get('username',instance.username)
		instance.first_name = validated_data.get('first_name',instance.first_name)
		instance.last_name = validated_data.get('last_name',instance.last_name)
		instance.email = validated_data.get('email',instance.email)
		instance.last_login = validated_data.get('last_login',instance.last_login)
		instance.set_password(validated_data.get('password',instance.password))
		instance.save()
		return instance

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Serializer Class for Student Model
	'''
	user_details = UserSerializer(source = 'user')
	relevent_count = serializers.ReadOnlyField(source='relevent')
	academics_count = serializers.ReadOnlyField(source='academics')
	administration_count = serializers.ReadOnlyField(source='administration')
	misc_count = serializers.ReadOnlyField(source='misc')
	tnp_count = serializers.ReadOnlyField(source='tnp')
	events_count = serializers.ReadOnlyField(source='events')

	class Meta:
		model = Student
		fields = ('user_details', 'id', 'univ_roll_no','ph_no','father_name','mother_name','address', 'course', 'relevent_count', 'academics_count', 'administration_count', 'tnp_count', 'events_count', 'misc_count', 'relevent_last_seen', 'administration_last_seen', 'academics_last_seen', 'misc_last_seen', 'tnp_last_seen', 'events_last_seen')

	def create(self, validated_data):
		"""
		Create and return a new `Student` instance, given the validated data.
		"""
		return Student.objects.create(**validated_data)

	def update(self, instance, validated_data):
		validated_user_data = validated_data['user'].items()
		user = User.objects.filter(username = validated_data['username'])
		user.update(email = validated_user_data[0][1], first_name = validated_user_data[2][1], last_name = validated_user_data[3][1])
		user[0].set_password(validated_user_data[1][1])
		instance.univ_roll_no = validated_data.get('univ_roll_no',instance.univ_roll_no)
		instance.ph_no = validated_data.get('ph_no',instance.ph_no)
		instance.father_name = validated_data.get('father_name',instance.father_name)
		instance.mother_name = validated_data.get('mother_name',instance.mother_name)
		instance.address = validated_data.get('address',instance.address)
		instance.course = validated_data.get('course',instance.course)
		instance.relevent_last_seen = validated_data.get('relevent_last_seen',instance.relevent_last_seen)
		instance.academics_last_seen = validated_data.get('academics_last_seen',instance.academics_last_seen)
		instance.administration_last_seen = validated_data.get('administration_last_seen',instance.administration_last_seen)
		instance.misc_last_seen = validated_data.get('misc_last_seen',instance.misc_last_seen)
		instance.tnp_last_seen = validated_data.get('tnp_last_seen',instance.tnp_last_seen)
		instance.events_last_seen = validated_data.get('events_last_seen',instance.events_last_seen)
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
	notices = serializers.HyperlinkedRelatedField(many=True, view_name='notice-detail', read_only=True)
	class Meta:
		model = Faculty
		fields = ('user_fields', 'notices', 'id','designation','department','ph_no','address', 'alternate_email','relevent_count', 'academics_count', 'administration_count', 'tnp_count', 'events_count', 'misc_count', 'relevent_last_seen', 'administration_last_seen', 'academics_last_seen', 'misc_last_seen', 'tnp_last_seen', 'events_last_seen')

	def create(self, validated_data):
		"""
		Create and return a new `Faculty` instance, given the validated data.
		"""
		return Faculty.objects.create(**validated_data)

	def update(self, instance, validated_data):
		validated_user_data = validated_data['user'].items()
		user = User.objects.filter(username = validated_data['username'])
		user.update(email = validated_user_data[0][1], first_name = validated_user_data[2][1], last_name = validated_user_data[3][1])
		user[0].set_password(validated_user_data[1][1])
		instance.designation = validated_data.get('designation',instance.designation)
		instance.department = validated_data.get('department',instance.department)
		instance.ph_no = validated_data.get('ph_no',instance.ph_no)
		instance.address = validated_data.get('address',instance.address)
		instance.alternate_email = validated_data.get('alternate_email',instance.alternate_email)
		instance.relevent_last_seen = validated_data.get('relevent_last_seen',instance.relevent_last_seen)
		instance.academics_last_seen = validated_data.get('academics_last_seen',instance.academics_last_seen)
		instance.administration_last_seen = validated_data.get('administration_last_seen',instance.administration_last_seen)
		instance.misc_last_seen = validated_data.get('misc_last_seen',instance.misc_last_seen)
		instance.tnp_last_seen = validated_data.get('tnp_last_seen',instance.tnp_last_seen)
		instance.events_last_seen = validated_data.get('events_last_seen',instance.events_last_seen)
		instance.save()
		return instance


class NoticeSerializer(serializers.ModelSerializer):
	'''
	Serializer Class for Notices Model
	'''
	owner = serializers.ReadOnlyField(source='owner.user.username')
	bookmark_flag = serializers.SerializerMethodField('check_for_bookmark_flag')
	bookmark_id = serializers.SerializerMethodField('check_for_bookmark_id')

	def check_for_bookmark_flag(self, Notice):
		if BookmarkedNotice.objects.filter(notice__id = Notice.id, user__id = self.context['request'].user.id ).count()==1:
			return True
		else:
			return False
	
	def check_for_bookmark_id(self, Notice):
		if BookmarkedNotice.objects.filter(notice = Notice.id ).count():
			return BookmarkedNotice.objects.get(notice = Notice.id ).id
		else:
			return None
	
	class Meta:
		model = Notice
		fields = ('owner', 'bookmark_flag', 'bookmark_id', 'id', 'scheduled_time','title','description','ce','cs','it','ee','ece','eee','me','mt','ic','first_year','second_year','third_year','fourth_year','btech','mtech','mba','mca','other_course','file_attached','created_at','updated_at', 'category', 'subject')

	def create(self, validated_data):
		"""
		Create and return a new `Notices` instance, given the validated data.
		"""
		return Notice.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.scheduled_time = validated_data.get('scheduled_time',instance.scheduled_time)
		instance.title = validated_data.get('title',instance.title)
		instance.description = validated_data.get('description',instance.description)
		instance.file_attached = validated_data.get('file_attached',instance.file_attached)
		instance.created_at = validated_data.get('created_at',instance.created_at)
		instance.updated_at = validated_data.get('updated_at',instance.updated_at)
		instance.category = validated_data.get('category',instance.category)
		instance.subject = validated_data.get('subject',instance.subject)
		instance.cs = validated_data.get('cs',instance.cs)
		instance.ce = validated_data.get('ce',instance.ce)
		instance.ee = validated_data.get('ee',instance.ee)
		instance.ece = validated_data.get('ece',instance.ece)
		instance.eee = validated_data.get('eee',instance.eee)
		instance.it = validated_data.get('it',instance.it)
		instance.ic = validated_data.get('ic',instance.ic)
		instance.me = validated_data.get('me',instance.me)
		instance.mt = validated_data.get('mt',instance.mt)
		instance.first_year = validated_data.get('first_year',instance.first_year)
		instance.second_year = validated_data.get('second_year',instance.second_year)
		instance.third_year = validated_data.get('third_year',instance.third_year)
		instance.fourth_year = validated_data.get('fourth_year',instance.fourth_year)
		instance.btech = validated_data.get('btech',instance.btech)
		instance.mtech = validated_data.get('mtech',instance.mtech)
		instance.mba = validated_data.get('mba',instance.mba)
		instance.mca = validated_data.get('mca',instance.mca)
		instance.other_course = validated_data.get('other_course',instance.other_course)
		instance.save()
		return instance


class NoticeListSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Serializer Class for Listing the notices only(not the details) that are available in Model
	'''
	owner = serializers.ReadOnlyField(source='owner.username')
	attachment_flag = serializers.SerializerMethodField('check_for_attachment')
	bookmark_flag = serializers.SerializerMethodField('check_for_bookmark_flag')
	
	def check_for_bookmark_flag(self, Notice):
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
	user = serializers.PrimaryKeyRelatedField(source='user.username', read_only = True)
	notice_id = serializers.SlugRelatedField(source='notice', slug_field = 'pk', queryset = Notice.objects.all())
	class Meta:
		model = BookmarkedNotice
		fields = ('id','user', 'notice_id')

	def create(self, validated_data):
		"""
		Create and return a new `BookmarkedNotice` instance, given the validated data.
		"""
		return BookmarkedNotice.objects.create( **validated_data)

	def update(self, instance, validated_data):
		instance.id = validated_data.get('id',instance.id)
		instance.user = validated_data.get('user',instance.user)
		# instance.notice = validated_data.get('notice',instance.notice)
		instance.save()
		return instance	
