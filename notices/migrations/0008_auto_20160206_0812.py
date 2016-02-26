# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0007_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticebranchyear',
            name='notice',
        ),
        migrations.AddField(
            model_name='notice',
            name='branch',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='course',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='semester',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='NoticeBranchYear',
        ),
    ]
