from django.db import models
from django.utils import timezone

from user_auth.models import User


# Create your models here.


class Address(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    rating = models.FloatField(default=None, null=True)
    image = models.ImageField(upload_to='restaurants')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"
        # ordering = ['name']

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField(max_length=500)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username + " " + self.restaurant.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"