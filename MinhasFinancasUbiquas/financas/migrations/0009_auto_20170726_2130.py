# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0008_lancamentofinanceiro_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamentofinanceiro',
            name='descricao',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True, verbose_name='Descrição'),
        ),
    ]