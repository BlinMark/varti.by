# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20170424_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(verbose_name='E-mail', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(verbose_name='Имя', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sername',
            field=models.CharField(verbose_name='Фамилия', max_length=20),
        ),
    ]
