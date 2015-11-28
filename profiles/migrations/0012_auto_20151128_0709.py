# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='branch',
            field=models.CharField(default=None, max_length=5, null=True, choices=[(b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'EEE', b'Electrical and Electronics Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology')]),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='course',
            field=models.CharField(default=None, max_length=5, null=True, choices=[(b'BT', b'B.Tech'), (b'MCA', b'MCA'), (b'MBA', b'MBA'), (b'MTECH', b'Masters of Technology'), (b'OT', b'Others')]),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='year',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
