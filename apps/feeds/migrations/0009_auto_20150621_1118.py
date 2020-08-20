# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0008_auto_20150621_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='user_id',
        ),
        migrations.AddField(
            model_name='faculty',
            name='user',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
