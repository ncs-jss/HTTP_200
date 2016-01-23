# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20160123_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='mid',
            field=models.ForeignKey(related_name='notification', verbose_name=b'Message Id', to='message.Message'),
        ),
    ]
