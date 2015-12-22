# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20151102_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetail',
            name='branch',
            field=models.CharField(default=None, max_length=5, choices=[(b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (
                b'EEE', b'Electrical and Electronics Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology')]),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='year',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='facultydetail',
            name='display_to_others',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='course',
            field=models.CharField(default=b'BT', max_length=3, choices=[(
                b'BT', b'B.Tech'), (b'MCA', b'MCA'), (b'MBA', b'MBA'), (b'MTECH', b'Masters of Technology'), (b'OT', b'Others')]),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='display_to_others',
            field=models.BooleanField(default=False),
        ),
    ]
