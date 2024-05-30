from django.db import models
from django.utils import timezone

from user_auth.models import User


# Create your models here.
class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок', max_length=200)
    subtitle = models.CharField('Подзаголовок', max_length=200)
    content = models.TextField('Текст статьи')
    date = models.DateField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    picture = models.ImageField(upload_to='articles/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
