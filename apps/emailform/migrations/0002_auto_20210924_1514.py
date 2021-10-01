# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emaildetail',
            old_name='hod_approved_email',
            new_name='hod_approval',
        ),
    ]
