# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0011_trendingincollege_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='trendingincollege',
            name='small_description',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
