# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0005_bookmarkednotice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticebranchyear',
            name='branch',
            field=models.CharField(default=b'ALL', max_length=5),
        ),
        migrations.AlterField(
            model_name='noticebranchyear',
            name='year',
            field=models.CharField(default=b'ALL', max_length=2),
        ),
    ]
