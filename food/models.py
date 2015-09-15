from django.db import models
from core.save_image import save_image


def food_category_images(instance, filename):
    return save_image('feed_category_images', filename)


def food_item_images(instance, filename):
    return save_image('feed_item_images', filename)


class FoodCategory(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to=food_category_images, null=True, blank=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=64)
    is_veg = models.BooleanField(default=True)
    categories = models.ManyToManyField(FoodCategory)
    image = models.ImageField(upload_to=food_item_images, null=True, blank=True)

    def __str__(self):
        return self.name

