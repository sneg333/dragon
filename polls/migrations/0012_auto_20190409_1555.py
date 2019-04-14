# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-09 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_usluga_title2_usluga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Katalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_katalog', models.CharField(max_length=200, verbose_name='каталог')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('image_catalog', models.ManyToManyField(blank=True, to='polls.Gallery', verbose_name='фотокаталог')),
            ],
            options={
                'verbose_name': 'каталог',
                'verbose_name_plural': 'каталог',
            },
        ),
        migrations.CreateModel(
            name='PodKatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_podkatalog', models.CharField(max_length=200, verbose_name='подкаталог')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('image_podkatalog', models.ImageField(blank=True, upload_to='podkatalog')),
                ('tovar_podkatalog', models.ManyToManyField(to='polls.Tovar', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'подкаталог',
                'verbose_name_plural': 'подкаталог',
            },
        ),
        migrations.AddField(
            model_name='katalog',
            name='podkatalog_katalog',
            field=models.ManyToManyField(blank=True, to='polls.PodKatalog', verbose_name='подкаталог'),
        ),
    ]
