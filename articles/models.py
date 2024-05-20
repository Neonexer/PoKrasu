from django.db import models
from django.utils import timezone


# Create your models here.
class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок', max_length=200)
    subtitle = models.CharField('Подзаголовок', max_length=200)
    content = models.TextField('Текст статьи')
    date = models.DateField('Дата публикации', default=timezone.now)
    # author = models.CharField(max_length=200)
    # picture = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
