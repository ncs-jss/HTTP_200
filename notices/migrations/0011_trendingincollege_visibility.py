# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0010_auto_20160206_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='trendingincollege',
            name='visibility',
            field=models.BooleanField(default=False),
        ),
    ]
