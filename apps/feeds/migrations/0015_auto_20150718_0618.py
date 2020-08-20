# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0014_auto_20150630_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='name',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='faculty_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='notice',
            name='owner',
            field=models.ForeignKey(related_name='notices', default=None, to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='alternate_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
