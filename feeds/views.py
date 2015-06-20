from django.shortcuts import render
from django.http import *
from couchbase.bucket import Bucket

cb = Bucket('couchbase:///infodb', password="123456")
print cb

def home(request):
	return HttpResponse("Hi there. It is working very fine.")

# Below the code is for the REST API

# from django.contrib.auth.models import User
from feeds.serializers import StudentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class StudentList(generics.ListCreateAPIView):
	# """
	# List all the Students or add Students 
	# """
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	permission_classes = (IsAdminUser,)
	paginate_by = 100

	def get_paginate_by(self):
		"""
		Use smaller pagination for HTML representations.
		"""
		if self.request.accepted_renderer.format == 'html':
			return 20
		return 100

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete an Student instance.
	"""
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	model = Student

class FacultyList(generics.ListCreateAPIView):
	"""
	List all the faculties or add faculties 
	"""
	queryset = Faculty.objects.all()
	serializer_class = FacultySerializer
	permission_classes = (IsAdminUser,)
	paginate_by = 100

	def get_paginate_by(self):
		"""
		Use smaller pagination for HTML representations.
		"""
		if self.request.accepted_renderer.format == 'html':
			return 20
		return 100

class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete an Faculty instance.
	"""
	queryset = Faculty.objects.all()
	serializer_class = FacultySerializer
	model = Faculty


class NoticeList(generics.ListCreateAPIView):
	"""
	List all the Notices or add Notices 
	"""
	queryset = Notice.objects.all()
	serializer_class = NoticeSerializer
	permission_classes = (IsAdminUser,)
	paginate_by = 100

	def get_paginate_by(self):
		"""
		Use smaller pagination for HTML representations.
		"""
		if self.request.accepted_renderer.format == 'html':
			return 20
		return 100

class NoticeDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a Notices instance.
	"""
	queryset = Notice.objects.all()
	serializer_class = NoticeSerializer
	model = Notice


class ScheduledNoticeList(generics.ListCreateAPIView):
	"""
	List all the Notices or add Notices 
	"""
	queryset = ScheduledNotice.objects.all()
	serializer_class = ScheduledNoticeSerializer
	permission_classes = (IsAdminUser,)
	paginate_by = 100

	def get_paginate_by(self):
		"""
		Use smaller pagination for HTML representations.
		"""
		if self.request.accepted_renderer.format == 'html':
			return 20
		return 100

class ScheduledNoticeDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a Scheduled Notices instance.
	"""
	queryset = ScheduledNotices.objects.all()
	serializer_class = ScheduledNoticeSerializer
	model = ScheduledNotice


