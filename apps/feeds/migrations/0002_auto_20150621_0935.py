# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='email',
            new_name='email_id',
        ),
    ]
