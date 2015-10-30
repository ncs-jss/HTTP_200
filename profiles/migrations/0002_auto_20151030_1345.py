# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('ph_no', models.PositiveIntegerField(null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('alternate_email', models.EmailField(max_length=254, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('univ_roll_no', models.PositiveIntegerField()),
                ('ph_no', models.PositiveIntegerField(null=True)),
                ('father_name', models.CharField(max_length=200, null=True)),
                ('mother_name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('course', models.CharField(default=b'BT', max_length=3, choices=[(b'BT', b'B.Tech'), (b'MCA', b'MCA'), (b'MBA', b'MBA'), (b'OT', b'Others')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='faculty1',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student1',
            name='user',
        ),
        migrations.DeleteModel(
            name='Faculty1',
        ),
        migrations.DeleteModel(
            name='Student1',
        ),
    ]
