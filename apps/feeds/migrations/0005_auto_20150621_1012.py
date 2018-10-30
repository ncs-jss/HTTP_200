# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20150621_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='password_reset',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='category',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password_reset',
        ),
        migrations.AddField(
            model_name='notice',
            name='course',
            field=models.CharField(default=b'MISC', max_length=4, choices=[(b'ACD', b'Academics'), (b'ADMN', b'Adminsitration'), (
                b'TNP', b'Training and Placement'), (b'EVNT', b'Events'), (b'MISC', b'Miscelleneous')]),
        ),
    ]
