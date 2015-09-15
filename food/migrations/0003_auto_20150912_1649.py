# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import food.models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_remove_fooditem_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=food.models.food_category_images),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=food.models.food_item_images),
        ),
    ]
