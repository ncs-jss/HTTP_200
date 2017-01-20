# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_student_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='email_id',
            field=models.EmailField(default=None, unique=True, max_length=254),
        ),
    ]
