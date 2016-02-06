from django.contrib import admin
from notices.models import Notice, BookmarkedNotice, TrendingInCollege
from profiles.models import FacultyDetail

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'title', 'courses', 'branches', 'semesters', 'created',)
    list_display_links = ('title', 'faculty')
    list_filter = ('faculty','category')
    list_per_page = 15
    #search_fields = ['title', 'faculty']

    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': ('faculty',('subject','category'), 'title', 'description', 'courses', 'branches', 'semesters',),
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


class TrendingInCollegeAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'visibility')
    
admin.site.register(Notice, NoticeAdmin)
admin.site.register(BookmarkedNotice, BookmarkedNoticeAdmin)
admin.site.register(TrendingInCollege, TrendingInCollegeAdmin)
