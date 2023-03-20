from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe


class Place(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    longitude = models.CharField(max_length=20, verbose_name='Долгота')
    latitude = models.CharField(max_length=20, verbose_name='Широта')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Полное описание')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.ImageField(verbose_name='Картинка')
    sequential_number = models.PositiveIntegerField(verbose_name='Порядковый номер', db_index=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['sequential_number']

    @property
    def absolute_url(self):
        return f'{settings.MEDIA_URL}{self.file}'

    @property
    def preview(self):
        height = min(200, self.file.height)
        width = self.file.width * height // self.file.height
        return mark_safe(f'<img src="{self.absolute_url}" width="{width}" height={height} />')

    def __str__(self):
        return self.file.name
