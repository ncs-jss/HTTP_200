from django.conf.urls import url
from notices.views import NoticeList, NoticeShow, NoticeCreateView, NoticeUpdateView, NoticeDeleteView, BookmarkCreateView,  BookmarkDeleteView, BookmarkListView, PinCreateView

urlpatterns = [
	url(r'(?P<pk>[0-9]+)/bookmark/$', BookmarkCreateView.as_view(), name='bookmark-add'),
	url(r'(?P<pk>[0-9]+)/bookmark/delete/$', BookmarkDeleteView.as_view(), name='bookmark-delete'),
	url(r'(?P<pk>[0-9]+)/edit/$', NoticeUpdateView.as_view(), name='notice_update'),
	url(r'(?P<pk>[0-9]+)/delete/$', NoticeDeleteView.as_view(), name='notice_delete'),
	url(r'(?P<pk>[0-9]+)/pinned/$', PinCreateView.as_view(), name='pin-add'),
	url(r'(?P<pk>[0-9]+)/', NoticeShow.as_view(), name = "notice_show"),
	url(r'^bookmark/$', BookmarkListView.as_view(), name='bookmark-list'),
	url(r'add/$', NoticeCreateView.as_view(), name='notice_add'),
	url(r'', NoticeList.as_view(), name = "notice_list"),
]
