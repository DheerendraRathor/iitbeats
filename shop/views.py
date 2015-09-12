from rest_framework import viewsets
from .models import Shop
from .serializers import ShopSerializer
from core.pagination import DefaultLimitOffsetPagination


class ShopViewsets(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    pagination_class = DefaultLimitOffsetPagination
