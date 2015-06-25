# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0006_auto_20150621_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='name',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_id',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notice',
            name='scheduled_time',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
