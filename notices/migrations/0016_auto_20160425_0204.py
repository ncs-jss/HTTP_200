# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0015_auto_20160312_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True),
        ),
    ]
