import uuid
import os

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

from apps.users.managers import CustomManager
from .services import get_upload_path, validate_file_extension


class Rename:
    def __init__(self, path):
        self.path = path;
        
    def rename(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), ext)
        return os.path.join(self.path, filename)


class User(AbstractUser):
    
    class Meta:
        # db_table = 'users_user'
        verbose_name = 'ПОЛЬЗОВАТЕЛЯ'
        verbose_name_plural = 'ПОЛЬЗОВАТЕЛИ'

    def __str__(self):
        return self.uniqueId.__str__();
    
    username = None;

    uniqueId = models.UUIDField(unique=True, verbose_name="Уникальный id", blank=True, null=True);

    logo = models.FileField(verbose_name='Загрузить фото *(150x150)', upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    email = models.EmailField(verbose_name='Почта', max_length=64, default=None, unique=True, blank=True, null=True)
    name = models.CharField(verbose_name='Имя', max_length=32)
    surname = models.CharField(verbose_name='Фамилия', max_length=32, blank=True, null=True)
    phone_one = models.CharField(verbose_name="Номер телефона", max_length=32, blank=True, null=True)
    dob = models.CharField(verbose_name='Дата рождения', max_length=16, blank=True, null=True)
    card = models.CharField(verbose_name='Номер дисконтной карты', max_length=16)
    password = models.CharField(verbose_name='Пароль', max_length=64)
    # REST_Password
    resetPasswordUUID = models.UUIDField(verbose_name="Ссылка для восстановления пароля", blank=True, null=True);
    resetPasswordDate = models.BigIntegerField(verbose_name="Время восстановления пароля", blank=True, null=True);
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    
    objects = CustomManager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.uniqueId = uuid.uuid4()
        super(User, self).save(force_insert=False, force_update=False, using=None, update_fields=None)