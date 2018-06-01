# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170918_2235'),
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
            name='newsletters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=25)),
                ('year', models.DateField()),
                ('paper', models.FileField(upload_to=b'newsletters')),
                ('created_at', models.DateTimeField()),
                ('modified_at', models.DateTimeField()),
                ('department', models.ForeignKey(to='newsletters.department')),
                ('uploaded_by', models.ForeignKey(to='profiles.FacultyDetail')),
            ],
        ),
    ]
