from django.contrib import admin
from . import models


class papers(admin.TabularInline):
	model = models.papers
	extra = 1


class department(admin.ModelAdmin):
	fields = ['department']
	inlines = [papers]


admin.site.register(models.department, department)
