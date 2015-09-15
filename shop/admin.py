from django.contrib import admin
from .models import Shop, Menu, Topping


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'phone', 'user']


class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'food_item', 'shop', 'price']


class ToppingAdmin(admin.ModelAdmin):
    list_display = ['id', 'food_item', 'menu', 'price']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Topping, ToppingAdmin)
