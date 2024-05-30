# Generated by Django 5.0.6 on 2024-05-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, upload_to='user/img'),
        ),
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
