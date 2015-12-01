# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20151030_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facultydetail',
            old_name='ph_no',
            new_name='contact_no',
        ),
        migrations.RenameField(
            model_name='studentdetail',
            old_name='ph_no',
            new_name='contact_no',
        ),
    ]
