# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20151112_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='year',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
