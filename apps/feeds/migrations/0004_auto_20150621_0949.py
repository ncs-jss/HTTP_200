# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_faculty_alternate_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='scheduled_time',
            field=models.DateTimeField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(default=b'BT', max_length=3, choices=[(
                b'BT', b'B.Tech'), (b'MCA', b'MCA'), (b'MBA', b'MBA'), (b'OT', b'Others')]),
        ),
    ]
