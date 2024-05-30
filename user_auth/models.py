from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    about = models.CharField(max_length=200, blank=True)
    img = models.ImageField(upload_to='user/img', blank=True)
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username