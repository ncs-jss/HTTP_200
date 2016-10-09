from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
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


class NoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeListSerializer
    pagination_class = NoticePageNumberPagination
    permission_class = [IsAuthenticated]
