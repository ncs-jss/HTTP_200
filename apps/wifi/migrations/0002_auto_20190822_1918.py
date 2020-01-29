# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wifi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wifidetail',
            name='laptop_mac_address',
        ),
        migrations.AddField(
            model_name='wifidetail',
            name='new_laptop_mac_address',
            field=models.CharField(default=None, max_length=200, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$', message=b'Enter MAC Address in Given Format.')]),
        ),
        migrations.AddField(
            model_name='wifidetail',
            name='old_laptop_mac_address',
            field=models.CharField(default=None, max_length=200, validators=[django.core.validators.RegexValidator(regex=b'^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$', message=b'Enter MAC Address in Given Format.')]),
        ),
    ]
