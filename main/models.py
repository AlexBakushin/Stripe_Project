from django.db import models


# Кастомный атрибут
NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    """
    Модель Товара
    """
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
