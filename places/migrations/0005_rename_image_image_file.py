# Generated by Django 4.1.7 on 2023-03-20 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_remove_place_coordinates_place_latitude_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='file',
        ),
    ]