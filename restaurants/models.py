from django.db import models

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=100)
    home = models.CharField(max_length=100)

    def __str__(self):
        return self.street + ", " + self.home

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    image = models.ImageField(upload_to='restaurants')

    def __str__(self):
        return self.name
