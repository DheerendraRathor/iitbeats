from rest_framework import serializers
from .models import FoodCategory, FoodItem


class FoodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodCategory


class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem
