# import datetime
from haystack import indexes
from feeds.models import *  # noqa ignore=F405
from datetime import datetime


class NoticeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    description = indexes.CharField(model_attr='description')
    details = indexes.CharField(model_attr='details')
    created_at = indexes.DateTimeField(model_attr='created_at')
    updated_at = indexes.DateTimeField(model_attr='updated_at')
    subject = indexes.CharField(model_attr='subject')
    owner = indexes.CharField(model_attr='owner')

    def get_model(self):
        return Notice

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_at__lte=datetime.now())
