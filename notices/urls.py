from django.conf.urls import url
from notices.views import (NoticeList, NoticeShow, CreateNotice, NoticeUpdateView, NoticeDeleteView,
                           BookmarkCreateView,  BookmarkDeleteView, BookmarkListView, PinCreateView, ReleventNoticeListView, SearchNotices)

urlpatterns = [
    url(r'(?P<pk>[0-9]+)/bookmark/$', BookmarkCreateView.as_view(), name='bookmark-add'),
    url(r'(?P<pk>[0-9]+)/bookmark/delete/$', BookmarkDeleteView.as_view(), name='bookmark-delete'),
    url(r'(?P<pk>[0-9]+)/edit/$', NoticeUpdateView.as_view(), name='notice_update'),
    url(r'(?P<pk>[0-9]+)/delete/$', NoticeDeleteView.as_view(), name='notice_delete'),
    url(r'(?P<pk>[0-9]+)/pinned/$', PinCreateView.as_view(), name='pin-add'),
    url(r'(?P<pk>[0-9]+)/', NoticeShow.as_view(), name="notice_show"),
    url(r'^bookmark/$', BookmarkListView.as_view(), name='bookmark-list'),
    url(r'^relevent/$', ReleventNoticeListView.as_view(), name="relevent_notice_list"),
    url(r'^search/$', SearchNotices.as_view(), name="notice_search"),
    url(r'add/$', CreateNotice.as_view(), name='notice_add'),
    url(r'', NoticeList.as_view(), name="notice_list"),
]
