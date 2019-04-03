# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-03 08:18
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_contact', models.CharField(max_length=200, verbose_name='контакт')),
                ('body_contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='текст')),
                ('adress_one_contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='первый адрес')),
                ('adress_toe_contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='второй адрес')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакт',
            },
        ),
        migrations.CreateModel(
            name='Dost_Oplat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_dostiop', models.CharField(max_length=200, verbose_name='доставка_и_оплата')),
                ('body_dostiop', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='текст')),
            ],
            options={
                'verbose_name': 'доставка_и_оплата',
                'verbose_name_plural': 'доставка_и_оплата',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_gallery', models.CharField(blank=True, max_length=150)),
                ('photo_gallery', models.ImageField(blank=True, upload_to='gallery', verbose_name='vse_gallery')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотогаллерея',
                'ordering': ('title_gallery',),
            },
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tovar', models.CharField(max_length=400, verbose_name='товар')),
                ('body_tovar', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='текст')),
                ('cena', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='цена')),
                ('body2_tovar', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='текст2')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товар',
            },
        ),
    ]