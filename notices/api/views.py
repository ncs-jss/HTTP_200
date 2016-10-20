from rest_framework.generics import (
    ListAPIView,
)

from rest_framework.permissions import(
    IsAuthenticated,
)

from notices.models import Notice

from .serializers import (
    NoticeListSerializer,
)

from .pagination import (
    NoticePageNumberPagination,
)

from rest_framework.views import APIView
from rest_framework.response import Response

class NoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeListSerializer
    pagination_class = NoticePageNumberPagination
    permission_class = [IsAuthenticated,]
