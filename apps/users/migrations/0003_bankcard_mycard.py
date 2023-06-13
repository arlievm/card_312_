# Generated by Django 3.2.9 on 2023-06-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numcard', models.IntegerField(max_length=64, verbose_name='Номер карты')),
                ('period', models.IntegerField(max_length=12, verbose_name='Срок действия карты')),
                ('name_plural', models.CharField(max_length=32, verbose_name='Имя владельца')),
                ('code', models.IntegerField(max_length=12, verbose_name='Код CVC/CVV')),
                ('email', models.EmailField(blank=True, default=None, max_length=64, null=True, unique=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Добавить банковскую карту ',
                'verbose_name_plural': 'Добавить банковскую карту ',
            },
        ),
        migrations.CreateModel(
            name='Mycard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Моя карта',
            },
        ),
    ]