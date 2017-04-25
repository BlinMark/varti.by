# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы', 'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=12, auto_now_add=True, verbose_name='Создан'),
            preserve_default=False,
        ),
    ]
