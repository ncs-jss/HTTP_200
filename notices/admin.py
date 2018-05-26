from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from notices.models import Notice, BookmarkedNotice, TrendingInCollege


class BookmarkedNoticeAdmin(admin.TabularInline):
    model = BookmarkedNotice
    extra = 1
    fieldsets = (
        (None, {
            'classes': ('extrapretty', 'wide'),
            'fields': (('user', 'notice'), 'pinned'),
        }),
    )


class NoticeAdmin(ImportExportModelAdmin):
    list_display = (
        'faculty', 'title', 'course_branch_year',
        'created', 'modified', 'visible_for_student',
        'visible_for_faculty', 'visible_for_hod',
        'visible_for_others', 'visible_for_management'
    )
    list_display_links = ('title', 'faculty')
    list_filter = ('faculty', 'category')
    list_per_page = 100
    inlines = [BookmarkedNoticeAdmin]
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'faculty', 'category', 'title', 'description',
                'file_attached', 'course_branch_year',
                'visible_for_student', 'visible_for_faculty',
                'visible_for_hod',
                'visible_for_others', 'visible_for_management', ),
        }),
    )


class TrendingInCollegeAdmin(ImportExportModelAdmin):
    list_display = ('title', 'attachment', 'visibility')


admin.site.register(Notice, NoticeAdmin)
admin.site.register(TrendingInCollege, TrendingInCollegeAdmin)
