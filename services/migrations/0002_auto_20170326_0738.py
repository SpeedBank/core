# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to='accounts.Branch'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='customer_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to='accounts.CustomerService'),
        ),
    ]