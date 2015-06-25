from django.contrib import admin
from django.contrib.auth.models import User
from feeds.models import *
# Register your models here.
# admin.site.unregister(User)
admin.site.register(Student)
admin.site.register(Faculty)
