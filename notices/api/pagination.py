from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)


class NoticePageNumberPagination(PageNumberPagination):
	page_size = 10