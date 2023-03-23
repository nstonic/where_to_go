from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    longitude = models.FloatField(max_length=20, verbose_name='Долгота')
    latitude = models.FloatField(max_length=20, verbose_name='Широта')
    description_short = models.TextField(verbose_name='Короткое описание', null=True, blank=True)
    description_long = HTMLField(verbose_name='Полное описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        unique_together = [['longitude', 'latitude']]

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

    def __str__(self):
        return self.file.name
