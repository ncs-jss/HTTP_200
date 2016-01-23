# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20160123_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
