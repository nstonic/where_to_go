from django.conf import settings
from django.db import models


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
    sequential_number = models.IntegerField(verbose_name='Порядковый номер')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    @property
    def get_absolute_image_url(self):
        return f'{settings.MEDIA_URL}{self.file}'

    def __str__(self):
        return f'{self.sequential_number} - {self.place}'
