# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20151128_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultydetail',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True),
        ),
        migrations.AddField(
            model_name='facultydetail',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True),
        ),
    ]
