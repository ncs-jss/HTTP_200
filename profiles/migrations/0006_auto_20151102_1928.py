# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20151031_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultydetail',
            name='address',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='facultydetail',
            name='alternate_email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='facultydetail',
            name='contact_no',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='facultydetail',
            name='department',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='facultydetail',
            name='designation',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='address',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='contact_no',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='father_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='mother_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='univ_roll_no',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
