from rest_framework.pagination import (
    PageNumberPagination,
)


class NoticePageNumberPagination(PageNumberPagination):
    page_size = 10
