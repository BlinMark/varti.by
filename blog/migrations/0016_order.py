# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170423_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(verbose_name='Имя', max_length=60)),
                ('phone', models.CharField(verbose_name='Телефон', max_length=20)),
                ('country', models.CharField(verbose_name='Страна', max_length=30)),
                ('area', models.CharField(verbose_name='Область', blank=True, null=True, max_length=30)),
                ('city', models.CharField(verbose_name='Город', max_length=30)),
                ('street', models.CharField(verbose_name='Улица', max_length=30)),
                ('home', models.CharField(verbose_name='Дом', max_length=30)),
                ('korpus', models.CharField(verbose_name='Корпус', blank=True, null=True, max_length=30)),
                ('flat', models.CharField(verbose_name='Квартира', max_length=30)),
                ('created', models.DateTimeField(verbose_name='Создан', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='Обновлен', auto_now=True)),
                ('paid', models.BooleanField(verbose_name='Оплачен', default=False)),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
                'ordering': ('-created',),
            },
        ),
    ]
