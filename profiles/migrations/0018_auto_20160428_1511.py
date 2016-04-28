# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetail',
            name='semester',
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='section',
            field=models.PositiveIntegerField(default=None, null=True, choices=[(b'CSE1', b'CSE1'), (b'CSE2', b'CSE2'), (b'IT1', b'IT1'), (b'IT2', b'IT2'), (b'ECE1', b'ECE1'), (b'ECE2', b'ECE2'), (b'EE1', b'EE1'), (b'EE2', b'EE2'), (b'CE1', b'CE1'), (b'CE2', b'CE2'), (b'ICE1', b'ICE1'), (b'ICE2', b'ICE2'), (b'MT1', b'MT1'), (b'MT2', b'MT2'), (b'ME1', b'ME1'), (b'ME2', b'ME2')]),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='year',
            field=models.PositiveIntegerField(default=None, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='display_to_others',
            field=models.BooleanField(default=True),
        ),
    ]
