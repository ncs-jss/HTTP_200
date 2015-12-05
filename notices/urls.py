from django.conf.urls import url
from notices.views import NoticeList, NoticeShow, NoticeCreateView, NoticeUpdateView, NoticeDeleteView, BookmarkCreateView,  BookmarkDeleteView

urlpatterns = [
	url(r'^$', NoticeList.as_view(), name = "notice_list"),
	url(r'(?P<pk>[0-9]+)/edit/$', NoticeUpdateView.as_view(), name='notice_update'),
	url(r'(?P<pk>[0-9]+)/delete/$', NoticeDeleteView.as_view(), name='notice_delete'),
	url(r'(?P<pk>[0-9]+)/', NoticeShow.as_view(), name = "notice_show"),
	url(r'add/$', NoticeCreateView.as_view(), name='notice_add'),
	url(r'(?P<pk>[0-9]+)/add_bookmark/$', BookmarkCreateView.as_view(), name='bookmark-add'), # handled via ajax
	url(r'(?P<pk>[0-9]+)/del_bookmark/$', BookmarkDeleteView.as_view(), name='bookmark-delete'), # handled via ajax
]
