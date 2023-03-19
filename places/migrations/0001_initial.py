# Generated by Django 4.1.7 on 2023-03-19 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.CharField(max_length=20, verbose_name='Долгота')),
                ('latitude', models.CharField(max_length=20, verbose_name='Широта')),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description_short', models.TextField(verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Полное описание')),
                ('coordinates', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='place', to='places.coordinates')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
    ]
