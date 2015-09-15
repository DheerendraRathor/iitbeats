# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import food.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to=food.models.food_category_images)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('is_veg', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to=food.models.food_item_images)),
                ('categories', models.ManyToManyField(to='food.FoodCategory')),
                ('toppings', models.ManyToManyField(to='food.FoodItem')),
            ],
        ),
    ]
