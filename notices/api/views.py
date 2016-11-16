from rest_framework import viewsets

from rest_framework.permissions import (
    IsAuthenticated,
)

from notices.models import Notice

from .serializers import (
    NoticeListSerializer,
    NoticeCreateSerializer,
)

from .pagination import (
    NoticePageNumberPagination,
)

from rest_framework.serializers import (
    ValidationError,
)
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from profiles.models import FacultyDetail
from rest_framework.mixins import ListModelMixin

User = get_user_model()


class NoticeListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    pagination_class = NoticePageNumberPagination
    serializer_class = NoticeListSerializer

    def get_queryset(self, **kwargs):
        user_group = self.request.user.groups.all()[0].name.lower()
        notices = Notice.objects.filter(**{'visible_for_'+user_group: True})
        category = self.request.META.get('HTTP_CATEGORY')
        username = self.request.META.get('HTTP_USERNAME')
        try:
            notice_id = self.kwargs["pk"]
        except:
            notice_id = None
        if notice_id:
            queryset = Notice.objects.filter(pk=notice_id)
            return queryset

        else:
            if username:
                if category == "none":
                    queryset = notices.order_by('-modified')
                    return queryset
                elif category == "":
                    raise ValidationError({"category": "This field can't be left blank."})
                else:
                    queryset = notices.filter(category=category).order_by('-modified')
                    return queryset
            else:
                raise ValidationError({"username": "This field can't be left blank."})


class NoticeCreateViewSet(APIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeCreateSerializer
    permission_classes = [IsAuthenticated, ]
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        user = self.request.META.get('HTTP_USERNAME')
        user = User.objects.filter(username=user)[0]
        if user.groups.all()[0].name.lower() == "student":
            raise ValidationError({"error": "Student Can't create notice."})
        else:
            try:
                serializer = NoticeCreateSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            except:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class MyUploadedNoticeViewSet(APIView, ListModelMixin):
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = NoticeCreateSerializer
    pagination_class = NoticePageNumberPagination

    def get(self, request):
        faculty = self.request.META.get('HTTP_FACULTY')
        if faculty:
            try:
                faculty = FacultyDetail.objects.filter(pk=faculty)[0]
                queryset = Notice.objects.filter(faculty=faculty).order_by('-modified')
                serializer = NoticeCreateSerializer(instance=queryset, many=True)
                return Response(serializer.data, status=HTTP_200_OK)
            except:
                raise ValidationError({"error": "There are no notices to show."})
        else:
            raise ValidationError({"faculty": "This filed can't be empty."})

# if user.groups.all()[0].name.lower() == "student":
#     raise ValidationError({"error": "Student Can't delete notice."})
# else:
#     try:
#         notice = self.get_object(pk)
#         notice.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
#     except:
#         return Response(status=HTTP_400_BAD_REQUEST)
