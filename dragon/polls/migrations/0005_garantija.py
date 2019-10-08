# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-03 15:39
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190403_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garantija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_garantija', models.CharField(max_length=200, verbose_name='гарантия')),
                ('body_garantija', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='гарантия')),
                ('body2_garantija', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='гарантия')),
            ],
            options={
                'verbose_name': 'гарантия',
                'verbose_name_plural': 'гарантия',
            },
        ),
    ]