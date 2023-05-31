from django.db import models

from .choices import Day
from .services import get_upload_path, validate_file_extension


class Partners(models.Model):
    
    class Meta:
        db_table = 'partners'
        verbose_name = 'ПАРТНЁРА'
        verbose_name_plural = 'ПАРТНЁРЫ'
        
    logo = models.FileField(verbose_name='Загрузить логотип *(150x150)', upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    image = models.FileField(verbose_name='Загрузить фонд *(305x210)', upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    mail = models.EmailField(verbose_name='Почта', max_length=64, blank=True, null=True)
    name = models.CharField(verbose_name='Наименование (брендовое название )', max_length=64)
    address = models.CharField(verbose_name='Адрес компании', max_length=64)
    org = models.CharField(verbose_name='Организационная праовая форма', max_length=64, blank=True, null=True)
    inn = models.CharField(verbose_name='ИНН', max_length=16, blank=True, null=True)
    activity_type = models.CharField(verbose_name='Тип деятельности', max_length=64)
    description = models.TextField(verbose_name='Описание компании')
    # Телефонный номер и социальные сети
    phone_one = models.CharField(verbose_name="Номера телефонов", max_length=32, blank=True, null=True)
    phone_two = models.CharField(verbose_name="", max_length=32, blank=True, null=True)
    phone_three = models.CharField(verbose_name="", max_length=32, blank=True, null=True)
    phone_four = models.CharField(verbose_name="", max_length=32, blank=True, null=True)
    ##########################################
    whatsapp = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    
    day = models.CharField(verbose_name="Режим работы", max_length=16, default=None, choices=Day, blank=True, null=True)
    data_time = models.DateTimeField(verbose_name='Режим работы', blank=True, null=True)
    
    def __str__(self):
        return self.name