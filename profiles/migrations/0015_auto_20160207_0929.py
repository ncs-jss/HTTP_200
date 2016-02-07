# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20160206_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdetail',
            old_name='year',
            new_name='semester',
        ),
    ]
