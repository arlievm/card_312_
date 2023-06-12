from django.db import models

class Feedback(models.Model):
    
    class Meta:
        verbose_name = 'Oбратная связь'
        verbose_name_plural = 'Oбратная связь'
        
    sms = models.TextField(verbose_name='Сообщение',blank=True,null=True)
    phone = models.CharField(verbose_name='Номер телефона',max_length=64)
    
    def __str__(self):
        return self.phone

    