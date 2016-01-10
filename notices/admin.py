from django.contrib import admin
from notices.models import Notice, BookmarkedNotice, NoticeBranchYear
from profiles.models import FacultyDetail

class NoticeAdmin(admin.ModelAdmin):
	list_display = ('faculty', 'created_at', 'title')
	list_display_links = ('title', 'faculty')
	list_filter = ('faculty','category')
	list_per_page = 15
	#search_fields = ['title', 'faculty']

	fieldsets = (
		(None, {
			'classes': ('wide', 'extrapretty'),
			'fields': ('faculty',('subject','category'),'title','description'),
		}),
	)

class NoticeBranchYearAdmin(admin.ModelAdmin):
	list_display = ('year', 'branch', 'notice')
	list_filter = ('faculty','category')
	list_display_links = ('notice',)
	list_filter = ('year','branch',)
	list_per_page = 20

	fieldsets = (
		(None, {
			'classes': ('extrapretty'),
			'fields': (('year','branch'),'notice'),
		}),
	)
	
class BookmarkedNoticeAdmin(admin.ModelAdmin):
	list_display = ('user', 'pinned', 'notice', )
	#list_filter = ('notice',)
	list_per_page = 25

	fieldsets = (
		(None, {
			'classes': ('extrapretty'),
			'fields': (('user','notice'),'pinned'),
		}),
	)
	
admin.site.register(Notice, NoticeAdmin)
admin.site.register(NoticeBranchYear, NoticeBranchYearAdmin)
admin.site.register(BookmarkedNotice, BookmarkedNoticeAdmin)
