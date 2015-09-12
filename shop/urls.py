from django.conf.urls import url, include
from .views import ShopViewsets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'shop', ShopViewsets)

urlpatterns = [
    url(r'api/', include(router.urls, namespace='shop_api'))
]