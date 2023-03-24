import json
import sys

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from urllib3.util import parse_url

from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('place_file', type=str)

    def handle(self, *args, **options):
        place_file = options['place_file']
        with open(place_file, encoding='utf8') as file:
            place_obj = json.load(file)
            place_title = place_obj['title']
        try:
            place, place_created = Place.objects.get_or_create(
                title=place_title,
                longitude=place_obj['coordinates']['lng'],
                latitude=place_obj['coordinates']['lat']
            )
        except IntegrityError:
            print('Ошибка записи. Объект с такими координатами уже существует в базе', file=sys.stderr)
            exit()
        else:
            if place_created:
                if not input('Такое место уже есть в базе. Обновить данные? y/n: ') in ['y', 'Y']:
                    exit()
            place.description_long = place_obj['description_long']
            place.description_short = place_obj['description_short']
            place.save()
            numbering_with = place.images.count() + 1
            img_urls = place_obj['imgs']
            for number, image_url in enumerate(img_urls, start=numbering_with):
                response = requests.get(image_url)
                try:
                    response.raise_for_status()
                except requests.exceptions.HTTPError:
                    continue

                image_file_name = parse_url(image_url).path.split('/')[-1]
                image = Image(place=place, sequential_number=number)
                image.file.save(
                    image_file_name.lower(),
                    ContentFile(response.content),
                    save=True
                )

