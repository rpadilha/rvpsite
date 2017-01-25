# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-25 14:28
from __future__ import unicode_literals

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
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('phone', models.CharField(max_length=11)),
                ('msg', models.CharField(max_length=700)),
                ('ipaddr', models.GenericIPAddressField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]