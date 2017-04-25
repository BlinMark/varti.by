# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20170424_2159'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
