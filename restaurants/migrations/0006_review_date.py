# Generated by Django 5.0.6 on 2024-05-31 10:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_alter_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]