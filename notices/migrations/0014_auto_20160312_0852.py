# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0013_auto_20160206_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='branches',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='semesters',
        ),
        migrations.AddField(
            model_name='notice',
            name='course_branch_sem',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
