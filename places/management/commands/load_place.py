import json
import sys
import textwrap
from hashlib import md5

import requests
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.core.validators import URLValidator

from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('place_url', type=str)

    def handle(self, *args, **options):
        place_url = options.get('place_url')
        validator = URLValidator()
        try:
            validator(place_url)
        except ValidationError:
            print('Неверный формат URL', file=sys.stderr)
            exit()

        response = requests.get(place_url)
        response.raise_for_status()
        place_obj = json.loads(response.content)
        place = create_place(place_obj)
        if img_urls := place_obj.get('imgs', []):
            add_images_to_place(
                img_urls=img_urls,
                place=place
            )


def create_place(place_obj: dict) -> Place:
    try:
        place, place_created = Place.objects.get_or_create(
            longitude=place_obj['coordinates']['lng'],
            latitude=place_obj['coordinates']['lat']
        )
    except KeyError:
        print('Не указаны координаты', file=sys.stderr)
        exit()
    else:
        if not place_created:
            if not input(textwrap.dedent("""
            Место с такими координатами уже есть в базе.
            Обновить данные? y/n: """)) in ['y', 'Y']:
                exit()
        place.title = place_obj.get(
            'title',
            'Название не указано'
        )
        place.description_long = place_obj.get(
            'description_long',
            'Описание не указано'
        )
        place.description_short = place_obj.get(
            'description_short',
            'Описание не указано'
        )
        place.save()
        return place


def add_images_to_place(img_urls: list, place: Place):
    numbering_with = place.images.count() + 1
    if numbering_with > 1:
        if input(textwrap.dedent("""
        У данного места уже есть изображения.
        Удалить их перед загрузкой новых? y/n: """)) in ['y', 'Y']:
            place.images.all().delete()
            numbering_with = 1
    for number, image_url in enumerate(img_urls, start=numbering_with):
        response = requests.get(image_url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(
                f'Не удалось скачать изображение: {image_url}',
                file=sys.stderr
            )
            continue

        image_file_name = md5(response.content).hexdigest()
        content_file = ContentFile(response.content, name=image_file_name)
        Image.objects.create(
            place=place,
            sequential_number=number,
            file=content_file
        )
