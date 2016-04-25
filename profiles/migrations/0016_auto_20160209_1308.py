# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20160207_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='course',
            field=models.CharField(default=None, max_length=5, null=True, choices=[(b'BTECH', b'B.Tech'), (b'MCA', b'MCA'), (b'MBA', b'MBA'), (b'MTECH', b'Masters of Technology'), (b'OTHER', b'Others')]),
        ),
    ]
