from django.shortcuts import render
from django.http import *
from couchbase.bucket import Bucket
from feeds.models import *
from feeds.serializers import *
from feeds.forms import *
from rest_framework import permissions

# cb = Bucket('couchbase:///infodb', password="123456")
# print cb

def home(request):
	return HttpResponse("<h1>Hi there. It is working very fine.</h1> {{ form.as_p }}")

def login(request):
	""" Login view """
	if not request.user.is_authenticated():
		if request.POST:
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				# Correct password, and the user is marked "active"
				auth.login(request,user)
				# Redirect to a success page.
				return HttpResponseRedirect("/")
			else:
				# Show an error page
				return HttpResponse("<h3>Incorrect password</h3>")
		return render_to_response('login.html',context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/profile")

def changepassword(request):
	""" user password change view """
	if user.is_authenticated:
		if request.POST:
			username = user.username
			# email = request.POST['email']
			password = request.POST['password']
			user = User.objects.get(username=username)
			user.set_password(password)
			user.save()
	return HttpResponseRedirect("/profile")


# Below the code is for the REST API

# from django.contrib.auth.models import User
from feeds.serializers import StudentSerializer
from rest_framework import generics
# from rest_framework.permissions import IsAdminUser

class StudentList(generics.ListCreateAPIView):
	# """
	# List all the Students or add Students 
	# """
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	# permission_classes = (IsAdminUser,)
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
	# permission_classes = (IsAdminUser,)
	# permission_classes = (IsAdminUser,)
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
	# permission_classes = (IsAdminUser,)
	# permission_classes = (permissions.IsAuthenticated,)
	paginate_by = 100

	def get_paginate_by(self):
		"""
		Use smaller pagination for HTML representations.
		"""
		if self.request.accepted_renderer.format == 'html':
			return 20
		return 100

	def perform_create(self, serializer):
		serializer.save(faculty_id=self.request.user)

class NoticeDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a Notices instance.
	"""
	queryset = Notice.objects.all()
	serializer_class = NoticeSerializer
	model = Notice
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class ScheduledNoticeList(generics.ListCreateAPIView):
# 	"""
# 	List all the Notices or add Notices 
# 	"""
# 	queryset = ScheduledNotice.objects.all()
# 	serializer_class = ScheduledNoticeSerializer
# 	permission_classes = (IsAdminUser,)
# 	paginate_by = 100

# 	def get_paginate_by(self):
# 		"""
# 		Use smaller pagination for HTML representations.
# 		"""
# 		if self.request.accepted_renderer.format == 'html':
# 			return 20
# 		return 100

# class ScheduledNoticeDetail(generics.RetrieveUpdateDestroyAPIView):
# 	"""
# 	Retrieve, update or delete a Scheduled Notices instance.
# 	"""
# 	queryset = ScheduledNotices.objects.all()
# 	serializer_class = ScheduledNoticeSerializer
# 	model = ScheduledNotice


from feeds.serializers import UserSerializer

from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer