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
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Message Date')),
                ('message', models.CharField(help_text=b'Please restrict the message length to 500.', max_length=500)),
                ('reciever', models.OneToOneField(related_name='Reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.OneToOneField(related_name='Sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent', models.BooleanField(default=True)),
                ('seen', models.BooleanField(default=False)),
                ('seen_at', models.DateTimeField()),
                ('mid', models.ForeignKey(verbose_name=b'Message Id', to='message.Message')),
            ],
        ),
    ]
