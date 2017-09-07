# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='tax_percentage',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='tax_total',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='line_item_total',
        ),
    ]
