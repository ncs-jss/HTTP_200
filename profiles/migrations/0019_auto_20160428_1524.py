# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20160428_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='branch',
            field=models.CharField(default=None, max_length=5, null=True, choices=[(b'None', None), (b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'EEE', b'Electrical and Electronics Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology')]),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='section',
            field=models.CharField(default=None, max_length=10, null=True, choices=[(b'None', None), (b'CSE1', b'CSE1'), (b'CSE2', b'CSE2'), (b'IT1', b'IT1'), (b'IT2', b'IT2'), (b'ECE1', b'ECE1'), (b'ECE2', b'ECE2'), (b'EE1', b'EE1'), (b'EE2', b'EE2'), (b'CE1', b'CE1'), (b'CE2', b'CE2'), (b'ICE1', b'ICE1'), (b'ICE2', b'ICE2'), (b'MT1', b'MT1'), (b'MT2', b'MT2'), (b'ME1', b'ME1'), (b'ME2', b'ME2')]),
        ),
    ]
