# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-04 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_zakaz'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='photo_tovar',
            field=models.ManyToManyField(blank=True, to='polls.Gallery', verbose_name='фото товара'),
        ),
        migrations.AlterField(
            model_name='tovar',
            name='title_tovar',
            field=models.CharField(max_length=400, verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
    ]
