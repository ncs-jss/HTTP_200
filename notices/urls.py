from django.conf.urls import url
from notices.views import NoticeList, NoticeDetailView, NoticeCreateView, NoticeUpdateView, NoticeDeleteView

urlpatterns = [
	url(r'^$', NoticeList.as_view(), name = "notice_list"),
	url(r'(?P<pk>[0-9]+)/$', NoticeDetailView.as_view(), name = "notice_detail"),
	url(r'add/$', NoticeCreateView.as_view(), name='notice_add'),
	url(r'/(?P<pk>[0-9]+)/edit/$', NoticeUpdateView.as_view(), name='notice_update'),
	url(r'/(?P<pk>[0-9]+)/delete/$', NoticeDeleteView.as_view(), name='notice_delete'),
]