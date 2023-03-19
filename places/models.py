from django.db import models


class Coordinates(models.Model):
    longitude = models.CharField(max_length=20, verbose_name='Долгота')
    latitude = models.CharField(max_length=20, verbose_name='Широта')

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'

    def __str__(self):
        return f'{self.longitude} : {self.latitude}'


class Place(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    coordinates = models.OneToOneField(Coordinates, on_delete=models.CASCADE, related_name='place')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title
