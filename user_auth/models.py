from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# class User(models.Model):
#     username = models.CharField("Имя пользователя", max_length=120, null=False, unique=True, default=None)
#     email = models.EmailField("Email", unique=True)
#     password = models.CharField("Password", max_length=120)
#
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"


class User(AbstractUser):
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username