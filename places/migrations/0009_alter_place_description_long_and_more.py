# Generated by Django 4.1.7 on 2023-03-23 07:46

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, null=True, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(max_length=20, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(max_length=20, verbose_name='Долгота'),
        ),
    ]
