from django.db import models

from restaurants.models import Restaurant
from user_auth.models import User


# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " - " + self.restaurant.name

    class Meta:
        unique_together = (('user', 'restaurant'),)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'