# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20150621_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='alternate_email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
