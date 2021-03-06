# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-10 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import rvpsite.contact.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-created_at',), 'verbose_name': 'MENSAGEM', 'verbose_name_plural': 'MENSAGENS'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ENVIADA EM'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=60, verbose_name='EMAIL'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ipaddr',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='ENDEREÇO IP'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.TextField(max_length=700, verbose_name='MENSAGEM'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, verbose_name='NOME'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=11, validators=[rvpsite.contact.validators.validate_phone], verbose_name='TELEFONE'),
        ),
    ]
