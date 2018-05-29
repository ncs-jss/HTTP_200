# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='papers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('year', models.DateField()),
                ('paper', models.FileField(upload_to=b'newsletters')),
                ('department', models.ForeignKey(to='newsletters.department')),
                ('uploaded_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
