# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0003_auto_20151128_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
