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
    image = models.ImageField(verbose_name='Фотография *(387x167)', upload_to='apps/images/product')
    discounts = models.CharField(verbose_name="Скидки", max_length=16, blank=True, null=True)
    name = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField(verbose_name='Описание')
    data = models.DateField(verbose_name="Дата", auto_now=False, auto_now_add=False)
    price = models.CharField(verbose_name="Цена", max_length=16)
    # quantity = models.PositiveIntegerField(default=0)
    # user_one = models.ForeignKey(Products,on_delete=models.CASCADE)
    
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
    

class Discountslider(models.Model):
    
    class Meta:
        db_table = "discount"
        verbose_name = "Баннер для Афиша"
        verbose_name_plural = "Баннер для Афиша"
        
    image = models.ImageField(verbose_name="Фотография",max_length=256)
    title = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return self.title
    
class Afishaslider(models.Model):
        
    class Meta:
        db_table = 'afisha'
        verbose_name = 'название описание картинка'
        verbose_name_plural = 'название описание картинка'
            
    photo = models.ImageField(verbose_name="Фотография *(1200x415)")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return self.description
    

    
    
    