from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField("Имя пользователя", max_length=120, null=False, unique=True, default=None)
    email = models.EmailField("Email", unique=True)
    password = models.CharField("Password", max_length=120)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"