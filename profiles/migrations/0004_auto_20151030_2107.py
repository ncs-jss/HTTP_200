# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20151030_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultydetail',
            name='display_to_others',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='display_to_others',
            field=models.BooleanField(default=True),
        ),
    ]
