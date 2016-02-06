# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0012_trendingincollege_small_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='updated_at',
        ),
    ]
