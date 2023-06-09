# Generated by Django 3.2.9 on 2023-05-31 09:43

import apps.partners.services
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=apps.partners.services.get_upload_path, validators=[apps.partners.services.validate_file_extension], verbose_name='Загрузить фонд *(305x210)'),
        ),
    ]
