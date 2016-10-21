from rest_framework.permissions import (
    IsAuthenticated,
)

from notices.models import Notice

from .serializers import (
    NoticeListSerializer,
)

# from .pagination import (
#     NoticePageNumberPagination,
# )
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core import serializers

User = get_user_model()


class NoticeListAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = NoticeListSerializer

    def get(self, request, *args, **kwargs):
        user_group = request.user.groups.all()[0].name.lower()
        notices = Notice.objects.filter(**{'visible_for_'+user_group: True})
        data = serializers.serialize('json', notices)
        return Response(data, status=HTTP_200_OK)
