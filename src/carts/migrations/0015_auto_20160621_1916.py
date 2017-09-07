# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0014_auto_20160621_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(default=0.085, max_digits=10, decimal_places=5),
        ),
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(default=25.0, max_digits=50, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=25.0, max_digits=50, decimal_places=2),
        ),
    ]
