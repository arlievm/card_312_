# Generated by Django 3.2.9 on 2023-06-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_playbill_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afishaslider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография *(1200x415)')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'название описание картинка',
                'verbose_name_plural': 'название описание картинка',
                'db_table': 'afisha',
            },
        ),
        migrations.CreateModel(
            name='Discountslider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=256, upload_to='', verbose_name='Фотография')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Баннер для Афиша',
                'verbose_name_plural': 'Баннер для Афиша',
                'db_table': 'discount',
            },
        ),
    ]
