# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField()),
                ('ph_no', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=500)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('bookmarks', jsonfield.fields.JSONField()),
                ('last_login', models.DateTimeField()),
                ('password_reset', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('details', jsonfield.fields.JSONField()),
                ('file_attached', jsonfield.fields.JSONField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('category', models.CharField(max_length=100)),
                ('scheduled_time', models.DateTimeField()),
                ('faculty_id', models.ForeignKey(to='feeds.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=100)),
                ('univ_roll_no', models.PositiveIntegerField()),
                ('ph_no', models.PositiveIntegerField()),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('email_id', models.EmailField(unique=True, max_length=254)),
                ('course', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField()),
                ('bookmarks', jsonfield.fields.JSONField()),
                ('last_login', models.DateTimeField()),
                ('password_reset', models.CharField(max_length=300)),
            ],
        ),
    ]
