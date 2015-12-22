# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20151112_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='course',
            field=models.CharField(default=None, max_length=5, null=True, choices=[(
                b'BT', b'B.Tech'), (b'MCA', b'MCA'), (b'MBA', b'MBA'), (b'MTECH', b'Masters of Technology'), (b'OT', b'Others')]),
        ),
    ]
