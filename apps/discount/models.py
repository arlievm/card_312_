from django.db import models

class Discounts(models.Model):
    
    class Meta:
        verbose_name = 'Все скидки '
        verbose_name_plural = 'Все скидки '
        
    image = models.ImageField(verbose_name="ФОТОГРАФИЯ *(387x167)", upload_to="apps/discount/images/")
    name = models.CharField(verbose_name="Наименование", max_length=50)
    description = models.TextField(verbose_name='Описание');
    
    
    
    def __str__(self):
        return self.name