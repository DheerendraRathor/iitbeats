from django.contrib import admin
from .models import FoodItem, FoodCategory


class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_veg', 'image']


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']


admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
