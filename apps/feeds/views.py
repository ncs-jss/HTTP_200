from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import *  # noqa ignore=F405

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from feeds.models import *  # noqa ignore=F405
from feeds.serializers import *  # noqa ignore=F405
from feeds.forms import *  # noqa ignore=F405
from feeds.permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyUser, HasGroupPermission, IsAuthenticatedUser


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


# Here I've used the ReadOnlyModelViewSet class to automatically provide the default 'read-only' operations
class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    permission_classes = (IsOwnerOrReadOnlyUser, )
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_update(self, serializer):
        user = self.request.user.username
        serializer.save(username=user)


# Here I've used the ReadOnlyModelViewSet class to automatically provide the default 'read-only' operations
class FacultyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    permission_classes = (IsOwnerOrReadOnlyUser,)
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

    def perform_update(self, serializer):
        user = self.request.user.username
        serializer.save(username=user)


# I've used the ModelViewSet class in order to get the complete set of default read and write operations
class NoticeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    permission_classes = (IsOwnerOrReadOnly,
                          HasGroupPermission)
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    required_groups = {
        'POST': ['Faculties'],
        'PUT': ['Faculties'],
        'DELETE': ['Faculties'],
    }
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category', 'description', 'title')

    def perform_create(self, serializer):
        user = self.request.user
        faculty = Faculty.objects.get(user__username=user.username)
        serializer.save(owner=faculty)

    def perform_update(self, serializer):
        user = self.request.user
        faculty = Faculty.objects.get(user__username=user.username)
        serializer.save(owner=faculty)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    permission_classes = (IsAuthenticatedUser,)
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


# I've used the ModelViewSet class in order to get the complete set of default read and write operations
class NoticeListViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` action.

    """
    permission_classes = (IsOwnerOrReadOnly,
                          HasGroupPermission)
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Notice.objects.all()
    serializer_class = NoticeListSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class BookmarkViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    permission_classes = (IsOwnerOrReadOnlyUser,)
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = BookmarkedNotice.objects.all()
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

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
