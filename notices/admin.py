from django.contrib import admin
from notices.models import Notice, BookmarkedNotice, NoticeBranchYear
# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
	list_display = ('title','faculty','category','created_at')

admin.site.register(Notice,NoticeAdmin)

class NoticeBranchYearAdmin(admin.ModelAdmin):
	list_display = ('notice', 'year', 'branch')

admin.site.register(NoticeBranchYear,NoticeBranchYearAdmin)

class BookmarkedNoticeAdmin(admin.ModelAdmin):
	list_display = ('user','notice')

admin.site.register(BookmarkedNotice,BookmarkedNoticeAdmin)
