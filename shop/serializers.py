from rest_framework import serializers
from .models import Shop, Menu, Topping
from core.serializers import UserSerializer
from food.serializers import FoodItemSerializer


class ShopSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Shop


class MenuSerializer(serializers.ModelSerializer):
    toppings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    food_item = FoodItemSerializer()

    class Meta:
        model = Menu


class ToppingSerializer(serializers.ModelSerializer):
    food_item = FoodItemSerializer()

    class Meta:
        model = Topping
