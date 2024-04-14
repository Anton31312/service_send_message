from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}

class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogs/', **NULLABLE, verbose_name='Изображение')
    date_is_published = models.DateField(default=timezone.now, verbose_name='Дата публикации')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовать')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
