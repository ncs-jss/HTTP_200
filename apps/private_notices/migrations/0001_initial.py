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
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent', models.BooleanField(default=False)),
                ('seen', models.BooleanField(default=False)),
                ('seen_at', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrivateNotice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'PrivateNotice Date')),
                ('pnotice', models.CharField(help_text=b'Please restrict the PrivateNotice length to 500.', max_length=500)),
                ('reciever', models.ForeignKey(related_name='Reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='Sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='mid',
            field=models.ForeignKey(related_name='notification', verbose_name=b'PrivateNotice Id',
                                    to='private_notices.PrivateNotice'),
        ),
    ]
