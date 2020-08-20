# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_auto_20150621_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='email_id',
            field=models.EmailField(default=None, unique=True, max_length=254),
        ),
        migrations.AddField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='user_id',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
