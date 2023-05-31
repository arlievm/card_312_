from django.db import models

from apps.categories.models import Category
from apps.partners.models import Partners


class Products(models.Model):
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    partners = models.ForeignKey(Partners, verbose_name="Партнёр", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фотография', upload_to='apps/images/product')
    discounts = models.CharField(verbose_name="Скидки", max_length=16, blank=True, null=True)
    name = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField(verbose_name='Описание')
    data = models.DateField(verbose_name="Дата", auto_now=False, auto_now_add=False)
    price = models.CharField(verbose_name="Цена", max_length=16)
    
    def __str__(self):
        return self.name
    

class Playbill(models.Model):

    class Meta:
        db_table = 'playbill'
        verbose_name = 'Афиша'
        verbose_name_plural = 'Афиша'

    image = models.ImageField(verbose_name='Фотография *(385x165)', upload_to='apps/images/playbill')
    title = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(verbose_name="Цена", max_length=16)

    def __str__(self):
        return self.title