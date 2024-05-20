# Generated by Django 5.0.6 on 2024-05-15 13:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]
