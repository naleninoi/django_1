from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=128, verbose_name='Название')
    image = models.ImageField(upload_to='products_images', blank=True, verbose_name='Изображение')
    short_desc = models.CharField(max_length=120, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')

    def __str__(self):
        return f'{self.name} ({self.category.name})'
