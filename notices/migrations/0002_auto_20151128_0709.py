# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticebranchyear',
            name='year',
            field=models.CharField(default=b'ALL', max_length=2, choices=[(
                1, b'First Year'), (2, b'Second Year'), (3, b'Third Year'), (4, b'Fourth Year'), (b'ALL', b'For all')]),
        ),
    ]
