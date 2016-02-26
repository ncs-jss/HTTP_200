# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0008_auto_20160206_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='course',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='semester',
        ),
        migrations.AddField(
            model_name='notice',
            name='branches',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='courses',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='semesters',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
