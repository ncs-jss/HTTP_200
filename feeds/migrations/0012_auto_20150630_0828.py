# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0011_faculty_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='file_attached',
            field=models.FileField(upload_to=b'attachments'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='scheduled_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
