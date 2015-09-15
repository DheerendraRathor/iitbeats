# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('is_available', models.BooleanField(default=True)),
                ('food_item', models.ForeignKey(to='food.FoodItem')),
                ('shop', models.ForeignKey(to='shop.Shop')),
            ],
        ),
    ]
