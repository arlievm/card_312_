# Generated by Django 3.2.9 on 2023-06-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_afishaslider_discountslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='apps/images/product', verbose_name='Фотография *(387x167)'),
        ),
    ]
