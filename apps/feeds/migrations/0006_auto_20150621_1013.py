# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0005_auto_20150621_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='course',
            new_name='category',
        ),
    ]
