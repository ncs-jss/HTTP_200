# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
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
                ('subject', models.CharField(max_length=200)),
                ('category', models.CharField(default=b'MISC', max_length=4, choices=[(b'ACD', b'Academics'), (b'ADMN', b'Administration'), (b'TNP', b'Training and Placement'), (b'EVNT', b'Events'), (b'MISC', b'Miscelleneous')])),
                ('course_branch_year', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True)),
                ('faculty', models.ForeignKey(to='profiles.FacultyDetail')),
            ],
        ),
        migrations.CreateModel(
            name='TrendingInCollege',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('small_description', models.CharField(max_length=200, null=True, blank=True)),
                ('url', models.URLField()),
                ('visibility', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bookmarkednotice',
            name='notice',
            field=models.ForeignKey(to='notices.Notice'),
        ),
        migrations.AddField(
            model_name='bookmarkednotice',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
