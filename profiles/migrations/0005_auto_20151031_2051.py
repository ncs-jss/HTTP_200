# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20151030_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='univ_roll_no',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
