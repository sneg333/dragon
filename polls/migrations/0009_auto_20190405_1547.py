# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-05 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190405_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='photo_tovar2',
        ),
        migrations.RemoveField(
            model_name='tovar',
            name='photo_tovar3',
        ),
        migrations.DeleteModel(
            name='Gallery2',
        ),
        migrations.DeleteModel(
            name='Gallery3',
        ),
    ]
