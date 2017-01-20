from django.contrib import admin
from django.contrib.auth.models import User
from feeds.models import *
from feeds.serializers import *
# Register your models here.
# admin.site.unregister(User)
# admin.site.register(Student)
# admin.site.register(Faculty)
# admin.site.register(Notice)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('univ_roll_no', 'ph_no', 'father_name', 'mother_name', 'address', 'course')

admin.site.register(Student, StudentAdmin)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('designation', 'department', 'ph_no', 'address', 'alternate_email')

admin.site.register(Faculty, FacultyAdmin)


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('scheduled_time', 'title', 'owner', 'description', 'ce', 'cs', 'it', 'ee', 'ece', 'eee', 'me', 'mt', 'ic', 'first_year', 'second_year',
                    'third_year', 'fourth_year', 'btech', 'mtech', 'mba', 'mca', 'other_course', 'file_attached', 'created_at', 'updated_at', 'category')

admin.site.register(Notice, NoticeAdmin)


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'notice')

admin.site.register(BookmarkedNotice, BookmarkAdmin)
