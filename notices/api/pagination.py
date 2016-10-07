from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)

class NoticeLimitOffSetPagination(LimitOffsetPagination):
	max_limit = 10


class NoticePageNumberPagination(PageNumberPagination):
	page_size = 10