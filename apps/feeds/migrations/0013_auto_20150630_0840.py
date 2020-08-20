# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0012_auto_20150630_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='faculty_id',
        ),
        migrations.AddField(
            model_name='notice',
            name='faculty',
            field=models.ForeignKey(related_name='notice_uploaded', default=True, to='feeds.Faculty', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
