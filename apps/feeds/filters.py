import django_filters
from feeds.models import Notice


class NoticeFilter(django_filters.FilterSet):
    owner = django_filters.CharFilter(name="owner__username")

    class Meta:
        model = Notice
        fields = ['category', 'in_stock', 'manufacturer']
