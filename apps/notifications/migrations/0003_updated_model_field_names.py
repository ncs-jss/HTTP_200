# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0002_added_default_notification_preferences'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationPreferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification_preferences', models.CharField(default=b'00000', max_length=200)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='user',
        ),
        migrations.RenameField(
            model_name='firebasetoken',
            old_name='user',
            new_name='user_id',
        ),
        migrations.DeleteModel(
            name='Preferences',
        ),
    ]
