# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('banner', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=205)),
                ('country', models.CharField(max_length=205)),
                ('latitude', models.FloatField(blank=True, default=0)),
                ('longitude', models.FloatField(blank=True, default=0)),
            ],
        ),
    ]
