# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0006_auto_20170725_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartaocredito',
            options={'ordering': ['numero'], 'verbose_name': 'Cartão de Crédito', 'verbose_name_plural': 'Cartões de Crédito'},
        ),
        migrations.AlterModelOptions(
            name='classificacao',
            options={'ordering': ['pk'], 'verbose_name': 'Classificação', 'verbose_name_plural': 'Classificações'},
        ),
        migrations.AlterModelOptions(
            name='lancamentofinanceiro',
            options={'ordering': ['pk'], 'verbose_name': 'Lançamento Financeiro', 'verbose_name_plural': 'Lançamentos Financeiros'},
        ),
        migrations.AddField(
            model_name='cartaocredito',
            name='data_fechamento_fatura',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de fechamento da fatura'),
        ),
        migrations.AddField(
            model_name='lancamentofinanceiro',
            name='descricao',
            field=models.CharField(default=' ', max_length=50, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='saque',
            name='valor_saque',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19, verbose_name='Valor saque'),
        ),
        migrations.AlterField(
            model_name='saque',
            name='descricao',
            field=models.CharField(default=' ', max_length=50, verbose_name='Descrição'),
        ),
    ]