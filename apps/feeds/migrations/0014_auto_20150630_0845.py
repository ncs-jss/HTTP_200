# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0013_auto_20150630_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='faculty',
        ),
        migrations.AddField(
            model_name='notice',
            name='faculty_id',
            field=models.ForeignKey(related_name='notice_uploaded', default=None, to='feeds.Faculty', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
