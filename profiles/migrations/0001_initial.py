# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('designation', models.CharField(max_length=100, null=True, blank=True)),
                ('department', models.CharField(max_length=100, null=True, blank=True)),
                ('contact_no', models.PositiveIntegerField(null=True, blank=True)),
                ('address', models.CharField(max_length=500, null=True, blank=True)),
                ('alternate_email', models.EmailField(max_length=254, null=True, blank=True)),
                ('display_to_others', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(default=None, max_length=5, null=True, choices=[(b'BTech', b'BTech'), (b'MCA', b'MCA'), (b'MBA', b'MBA'), (b'MTech', b'MTech'), (b'OTHER', b'Others')])),
                ('branch', models.CharField(default=None, max_length=5, null=True, choices=[(b'AllBranches', b'None'), (b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'EEE', b'Electrical and Electronics Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology')])),
                ('year', models.PositiveIntegerField(default=1, null=True, blank=True)),
                ('section', models.CharField(default=None, max_length=10, null=True, choices=[(b'AllSections', b'None'), (b'CSE1', b'CSE1'), (b'CSE2', b'CSE2'), (b'IT1', b'IT1'), (b'IT2', b'IT2'), (b'ECE1', b'ECE1'), (b'ECE2', b'ECE2'), (b'EE1', b'EE1'), (b'EE2', b'EE2'), (b'CE1', b'CE1'), (b'CE2', b'CE2'), (b'ICE1', b'ICE1'), (b'ICE2', b'ICE2'), (b'MT1', b'MT1'), (b'MT2', b'MT2'), (b'ME1', b'ME1'), (b'ME2', b'ME2')])),
                ('univ_roll_no', models.PositiveIntegerField(null=True, blank=True)),
                ('contact_no', models.PositiveIntegerField(null=True, blank=True)),
                ('father_name', models.CharField(max_length=200, null=True, blank=True)),
                ('mother_name', models.CharField(max_length=200, null=True, blank=True)),
                ('address', models.CharField(max_length=500, null=True, blank=True)),
                ('display_to_others', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
