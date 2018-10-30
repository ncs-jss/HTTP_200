# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='notification_preferences',
            field=models.CharField(default=b'00000', max_length=200),
        ),
    ]
