# from django.contrib import admin
# from notices.models import Notice, BookmarkedNotice, TrendingInCollege
# from import_export.admin import ImportExportModelAdmin


# class NoticeAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'faculty', 'title', 'course_branch_year', 'created', 'modified', 'visible_for_student',
#                     'visible_for_faculty', 'visible_for_hod', 'visible_for_others', 'visible_for_management'
#                     )
#     list_display_links = ('title', 'faculty')
#     list_filter = ('category',)
#     list_per_page = 15
#     # search_fields = ['title', 'faculty']

#     fieldsets = (
#         (None, {
#             'classes': ('wide', 'extrapretty'),
#             'fields': ('faculty', 'category', 'title', 'description', 'file_attached', 'course_branch_year', 'visible_for_student', 'visible_for_faculty', 'visible_for_hod', 'visible_for_others', 'visible_for_management', ),
#         }),
#     )


# class BookmarkedNoticeAdmin(ImportExportModelAdmin):
#     list_display = ('user', 'pinned', 'notice', )
#     # list_filter = ('notice',)
#     list_per_page = 25

#     fieldsets = (
#         (None, {
#             'classes': ('extrapretty'),
#             'fields': (('user', 'notice'), 'pinned'),
#         }),
#     )


# class TrendingInCollegeAdmin(ImportExportModelAdmin):
#     list_display = ('title', 'attachment', 'visibility')


# admin.site.register(Notice, NoticeAdmin)
# admin.site.register(BookmarkedNotice, BookmarkedNoticeAdmin)
# admin.site.register(TrendingInCollege, TrendingInCollegeAdmin)
