# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WifiDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('laptop_mac_address', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(regex=b'^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$', message=b'Enter MAc Address in Given Format.')])),
                ('mac_registered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
