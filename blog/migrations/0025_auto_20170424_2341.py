# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20170424_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='Example@varti.by', max_length=30, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=23, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='order',
            name='product_kreplenie',
            field=models.CharField(default=0, max_length=50, choices=[('Клейкая лента (1 р.)', 'Клейкая лента (1 р.)'), ('Липучки нарезные (2 р.)', 'Липучки нарезные (2 р.)'), ('Липучки готовые (5 р.)', 'Липучки готовые (5 р.)'), ('Верёка + крючёк (7 р.)', 'Верёка + крючёк (7 р.)')], verbose_name='Способ крепления'),
        ),
        migrations.AddField(
            model_name='order',
            name='sername',
            field=models.CharField(default='Ваша фамилия', max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='Ваше имя', max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_format',
            field=models.CharField(default=0, max_length=50, choices=[('Картина', 'Картина'), ('Постер', 'Постер')], verbose_name='Формат'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_orientation',
            field=models.CharField(default=0, max_length=50, choices=[('Горизонтальная', 'Горизонтальная'), ('Вертикальная', 'Вертикальная')], verbose_name='Ориентация'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_size',
            field=models.CharField(default=2, max_length=50, choices=[('A0 80*120 см. (80 р.)', 'A0 80*120 см. (80 р.)'), ('A1 60*80 см. (70 р.)', 'A1 60*80 см. (70 р.)'), ('A2 40*60 см. (60 р.)', 'A2 40*60 см. (60 р.)'), ('A3 30*40 см (50 р.)', 'A3 30*40 см (50 р.)'), ('A4 20*30 см. (40 р.)', 'A4 20*30 см. (40 р.)')], verbose_name='Размер'),
        ),
    ]
