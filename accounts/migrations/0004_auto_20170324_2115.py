# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 21:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=20)),
                ('speed_number', models.CharField(max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('profile_image', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_services', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_service', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bank',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bank',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='banner',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bank',
            name='logo',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', to='accounts.Bank'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', to=settings.AUTH_USER_MODEL),
        ),
    ]