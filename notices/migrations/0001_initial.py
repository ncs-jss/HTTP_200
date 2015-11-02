# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20151030_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('file_attached', models.FileField(null=True, upload_to=b'attachments', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=200)),
                ('category', models.CharField(default=b'MISC', max_length=4, choices=[(b'ACD', b'Academics'), (b'ADMN', b'Adminsitration'), (b'TNP', b'Training and Placement'), (b'EVNT', b'Events'), (b'MISC', b'Miscelleneous')])),
                ('faculty', models.ForeignKey(to='profiles.FacultyDetail')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeBranchYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.PositiveIntegerField(default=1)),
                ('branch', models.CharField(default=b'ALL', max_length=5, choices=[(b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'EEE', b'Electrical and Electronics Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology'), (b'MCA', b'Masters of Computer Applications'), (b'MBA', b'Master of Business Adminsitration  '), (b'MTECH', b'Masters of Technology'), (b'ALL', b'All branches and Courses')])),
                ('notice', models.ForeignKey(to='notices.Notice')),
            ],
        ),
    ]
