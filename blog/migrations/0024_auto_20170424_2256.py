# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_remove_order_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_format',
            field=models.CharField(default=0, verbose_name='Формат', max_length=2, choices=[('Картина', 'Картина'), ('Постер', 'Постер')]),
        ),
        migrations.AddField(
            model_name='order',
            name='product_orientation',
            field=models.CharField(default=0, verbose_name='Ориентация', max_length=2, choices=[('Горизонтальная', 'Горизонтальная'), ('Вертикальная', 'Вертикальная')]),
        ),
        migrations.AddField(
            model_name='order',
            name='product_size',
            field=models.CharField(default=0, verbose_name='Размер', max_length=2, choices=[('A0', 'A0'), ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4')]),
        ),
    ]
