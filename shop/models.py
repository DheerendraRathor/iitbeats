from django.db import models
from django.contrib.auth.models import User
from food.models import FoodItem


class Shop(models.Model):
    name = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Menu(models.Model):
    food_item = models.ForeignKey(FoodItem)
    shop = models.ForeignKey(Shop)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return '%s: %s' % (self.shop.name, self.food_item.name)


class Topping(models.Model):
    menu = models.ForeignKey(Menu, related_name='toppings')
    food_item = models.ForeignKey(FoodItem)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return '%s: %s' % (self.menu, self.food_item.name)


class Order(models.Model):
    ORDER_STATUS = [
        ('accepted', 'accepted'),
        ('declined', 'declined'),
        ('pending', 'pending'),
        ('completed', 'completed')
    ]

    user = models.ForeignKey(User)
    shop = models.ForeignKey(Shop)
    status = models.CharField(max_length=16, choices=ORDER_STATUS, default='pending')
    message = models.TextField()
    order_time = models.DateTimeField(auto_created=True)
    order_update = models.DateTimeField(auto_now=True)
    accept_time = models.DateTimeField(null=True, blank=True)
    completed_time = models.DateTimeField(null=True, blank=True)


class OrderItem(models.Model):
    QUANTITY_CHOICES = [(i, i) for i in range(1, 11)]

    food_item = models.ForeignKey(FoodItem)
    order = models.ForeignKey(Order)
    quantity = models.IntegerField(choices=QUANTITY_CHOICES, default=1)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    toppings = models.ManyToManyField(FoodItem)
