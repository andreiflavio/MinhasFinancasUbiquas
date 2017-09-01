# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0002_auto_20170901_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saque',
            name='conta',
        ),
        migrations.AlterField(
            model_name='lancamentofinanceiro',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Não Pago'), (1, 'Pago')], default='1', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='lancamentofinanceiro',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'A Receber'), (2, 'A Pagar')], verbose_name='Tipo'),
        ),
        migrations.DeleteModel(
            name='Saque',
        ),
    ]