# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20160123_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='seen_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
