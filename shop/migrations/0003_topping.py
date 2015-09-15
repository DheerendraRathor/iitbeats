# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20150912_1649'),
        ('shop', '0002_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('is_available', models.BooleanField(default=True)),
                ('food_item', models.ForeignKey(to='food.FoodItem')),
                ('menu', models.ForeignKey(to='shop.Menu', related_name='toppings')),
            ],
        ),
    ]
