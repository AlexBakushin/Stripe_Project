from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
     Регистрация в админке товара
    """
    list_display = ('id', 'name', 'description', 'price',)
    list_filter = ('name', 'price',)
    search_fields = ('name',)
