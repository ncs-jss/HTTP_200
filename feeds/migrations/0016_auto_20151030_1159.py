# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0015_auto_20150718_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkedNotice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='bookmarks',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='details',
        ),
        migrations.RemoveField(
            model_name='student',
            name='bookmarks',
        ),
        migrations.AddField(
            model_name='notice',
            name='btech',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='ce',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='cs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='ece',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='ee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='eee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='first_year',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='fourth_year',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='ic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='it',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='mba',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='mca',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='me',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='mt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='mtech',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='other_course',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='second_year',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='third_year',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='alternate_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='ph_no',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='file_attached',
            field=models.FileField(null=True, upload_to=b'attachments', blank=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='owner',
            field=models.ForeignKey(related_name='notices', default=None, to='feeds.Faculty'),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ph_no',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bookmarkednotice',
            name='notice',
            field=models.ForeignKey(to='feeds.Notice'),
        ),
        migrations.AddField(
            model_name='bookmarkednotice',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
