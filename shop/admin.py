from django.contrib import admin
from .models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'address', 'phone', 'user']


admin.site.register(Shop, ShopAdmin)
