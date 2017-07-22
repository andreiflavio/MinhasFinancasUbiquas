# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('ehContaBancaria', models.BooleanField(verbose_name='É uma conta bancária')),
            ],
        ),
        migrations.AlterField(
            model_name='classificacao',
            name='nome',
            field=models.CharField(max_length=80, verbose_name='Nome'),
        ),
    ]
