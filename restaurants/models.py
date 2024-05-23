from django.db import models

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
