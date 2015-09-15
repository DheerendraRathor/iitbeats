from rest_framework import viewsets
from .models import Shop, Menu, Topping
from .serializers import ShopSerializer, MenuSerializer, ToppingSerializer
from core.pagination import DefaultLimitOffsetPagination
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from food.serializers import FoodCategorySerializer


class ShopViewsets(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    pagination_class = DefaultLimitOffsetPagination

    @detail_route()
    def menu(self, request, pk=None):
        shop = get_object_or_404(Shop, pk=pk)
        menu = Menu.objects.all().filter(shop=shop).prefetch_related(
            'food_item__categories'
        )
        categories = set()
        for menu_item in menu:
            categories.update(menu_item.food_item.categories.all())
        toppings = Topping.objects.all().filter(menu__shop=shop).prefetch_related('food_item')
        menu_serialized = MenuSerializer(menu, many=True).data
        categories_serialized = FoodCategorySerializer(categories, many=True).data
        toppings_serialized = ToppingSerializer(toppings, many=True).data
        response_data = {
            'categories': categories_serialized,
            'menu': menu_serialized,
            'toppings': toppings_serialized,
        }
        return Response(response_data)

    @detail_route()
    def make_order(self, request, pk=None):
        shopt = get_object_or_404(Shop, pk=pk)
