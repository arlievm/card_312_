from django.db import models
# from apps.contact.models import Contacts

class Contacts(models.Model):
    
    class Meta:
        db_table = ''
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    name = models.CharField(verbose_name='Ф.И.О',max_length=64)
    phone = models.CharField(verbose_name='Телефон',max_length=36)
    email = models.EmailField(verbose_name='Почта',max_length=64)

    def __str__(self):
        return self.name



