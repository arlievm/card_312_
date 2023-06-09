# Generated by Django 3.2.9 on 2023-06-09 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20230608_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='post',
        ),
        migrations.AddField(
            model_name='favorites',
            name='like',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.like'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favorites',
            name='name_one',
            field=models.CharField(default=1, max_length=999, verbose_name='Oписание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='like',
            name='title',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='favorites',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
