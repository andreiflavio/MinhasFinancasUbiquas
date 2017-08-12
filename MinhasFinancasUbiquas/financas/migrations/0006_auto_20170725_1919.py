# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('financas', '0005_auto_20170721_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='LancamentoFinanceiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'A Receber'), ('2', 'A Pagar')], max_length=1)),
                ('data_emissao', models.DateField(verbose_name='Data emissão')),
                ('data_pagto', models.DateField(blank=True, null=True, verbose_name='Data pagamento')),
                ('cartaoCredito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financas.CartaoCredito')),
                ('classificacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financas.Classificacao')),
                ('conta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financas.Conta')),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Saque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('data_saque', models.DateTimeField(verbose_name='Data do saque')),
                ('conta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financas.Conta')),
            ],
        ),
        migrations.AddField(
            model_name='lancamentofinanceiro',
            name='saque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financas.Saque'),
        ),
    ]