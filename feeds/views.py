from django.contrib.auth.models import User, Group
from django.shortcuts import render, render_to_response
from django.http import *
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from feeds.models import *
from feeds.serializers import *
from feeds.forms import *
from feeds.permissions import IsOwnerOrReadOnly, HasGroupPermission

import django_filters

def home(request):
	return render_to_response("index.html")

@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'notices': reverse('notice-list', request=request, format=format),
		'students': reverse('student-list', request=request, format=format),
		'faculties': reverse('faculty-list', request=request, format=format),

	})


class StudentViewSet(viewsets.ReadOnlyModelViewSet): # Here I've used the ReadOnlyModelViewSet class to automatically provide the default 'read-only' operations
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	"""
	permission_classes = (IsOwnerOrReadOnly,)
	authentication_classes = (JSONWebTokenAuthentication, )
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class FacultyViewSet(viewsets.ReadOnlyModelViewSet): # Here I've used the ReadOnlyModelViewSet class to automatically provide the default 'read-only' operations
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	"""
	permission_classes = (IsOwnerOrReadOnly,)
	authentication_classes = (JSONWebTokenAuthentication, )
	queryset = Faculty.objects.all()
	serializer_class = FacultySerializer



class NoticeViewSet(viewsets.ModelViewSet):  # I've used the ModelViewSet class in order to get the complete set of default read and write operations
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	"""
	permission_classes = (IsOwnerOrReadOnly, 
		HasGroupPermission )
	# authentication_classes = (JSONWebTokenAuthentication, )
	queryset = Notice.objects.all()
	serializer_class = NoticeSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	required_groups = {
		'POST': ['Faculties'],
	}

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides `list` and `detail` actions.
	"""
	permission_classes = (IsOwnerOrReadOnly,)
	authentication_classes = (JSONWebTokenAuthentication, )
	queryset = User.objects.all()
	serializer_class = UserSerializer

class NoticeListViewSet(viewsets.ModelViewSet):  # I've used the ModelViewSet class in order to get the complete set of default read and write operations
	"""
	This viewset automatically provides `list` action.

	"""
	permission_classes = (IsOwnerOrReadOnly, 
		HasGroupPermission )
	authentication_classes = (JSONWebTokenAuthentication, )
	queryset = Notice.objects.all()
	serializer_class = NoticeListSerializer
	filter_backends = (filters.DjangoFilterBackend,)

# class check(APIView):
#     permission_classes = (IsAuthenticated, )
#     authentication_classes = (JSONWebTokenAuthentication, )
 
#     def get(self, request):
#     	group = None
#     	if User.objects.filter(groups__name='student'):
#     		group = "student"
#     	else:
#     		group = "faculty"
#         data = {
#             'id': request.user.id,
#             'username': request.user.username,
#             'token': str(request.auth),
#             'type' : group
#         }
#         return Response(data)