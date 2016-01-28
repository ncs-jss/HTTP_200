# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20160123_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='mid',
            field=models.ForeignKey(related_name='messages', verbose_name=b'Message Id', to='message.Message'),
        ),
    ]
