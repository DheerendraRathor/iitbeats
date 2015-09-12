from rest_framework import serializers
from .models import Shop
from core.serializers import UserSerializer


class ShopSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Shop