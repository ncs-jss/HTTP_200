# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0016_auto_20160425_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='course_branch_sem',
            new_name='course_branch_year',
        ),
    ]
