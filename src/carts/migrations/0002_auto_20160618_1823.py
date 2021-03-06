# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=1, to='carts.Cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='products.Variation', through='carts.CartItem'),
        ),
    ]
