# Generated by Django 5.0.6 on 2024-05-23 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='home',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street',
        ),
    ]