# Generated by Django 3.2.9 on 2023-06-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20230609_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.BooleanField(default=False),
        ),
    ]
