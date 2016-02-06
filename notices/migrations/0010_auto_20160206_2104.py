# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0009_auto_20160206_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendingInCollege',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bookmarkednotice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True),
        ),
        migrations.AddField(
            model_name='bookmarkednotice',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Created', null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Last Modified', null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='category',
            field=models.CharField(default=b'MISC', max_length=4, choices=[(b'ACD', b'Academics'), (b'ADMN', b'Administration'), (b'TNP', b'Training and Placement'), (b'EVNT', b'Events'), (b'MISC', b'Miscelleneous')]),
        ),
    ]
