# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
            field=models.ForeignKey(related_name='notice_uploaded', default=None, to='feeds.Faculty'),
        ),
    ]
