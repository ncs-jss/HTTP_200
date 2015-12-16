# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0005_bookmarkednotice'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarkednotice',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
