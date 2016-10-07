from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    )

from rest_framework.permissions import(
    IsAuthenticated,
    AllowAny,
    )

from notices.models import Notice 

from .serializers import (
    NoticeListSerializer,
    )

from .pagination import NoticeLimitOffSetPagination, NoticePageNumberPagination

class NoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeListSerializer
    permission_class = [AllowAny]
