# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkedNotice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pinned', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', ckeditor.fields.RichTextField()),
                ('file_attached', models.FileField(null=True, upload_to=b'attachments', blank=True)),
                ('category', models.CharField(default=b'misc', max_length=15, choices=[(b'academics', b'Academics'), (b'administration', b'Administration'), (b'tnp', b'Training and Placement'), (b'events', b'Events'), (b'misc', b'Miscelleneous')])),
                ('visible_for_student', models.BooleanField(default=True)),
                ('visible_for_hod', models.BooleanField(default=True)),
                ('visible_for_faculty', models.BooleanField(default=True)),
                ('visible_for_management', models.BooleanField(default=True)),
                ('visible_for_others', models.BooleanField(default=True)),
                ('course_branch_year', models.CharField(default=b'AllCourses-AllBranches-AllYears-AllSections', max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True)),
                ('faculty', models.ForeignKey(to='profiles.FacultyDetail', on_delete=django.db.models.deletion.SET_NULL)),
            ],
        ),
        migrations.CreateModel(
            name='TrendingInCollege',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('small_description', models.CharField(max_length=200, null=True, blank=True)),
                ('attachment', models.FileField(null=True, upload_to=b'trending', blank=True)),
                ('visibility', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bookmarkednotice',
            name='notice',
            field=models.ForeignKey(to='notices.Notice', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='bookmarkednotice',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
