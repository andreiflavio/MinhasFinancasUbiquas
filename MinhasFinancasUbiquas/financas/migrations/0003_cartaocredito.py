# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0002_auto_20170721_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartaoCredito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=80, verbose_name='Descrição')),
                ('numero', models.CharField(max_length=80, verbose_name='Número do Cartão de Crédito')),
                ('observacao', models.TextField(verbose_name='Observação')),
            ],
        ),
    ]
