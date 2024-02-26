from rest_framework import serializers
from main.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Сериализатор товара
    """
    class Meta:
        model = Item
        fields = '__all__'
