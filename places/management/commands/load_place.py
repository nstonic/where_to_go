import json
import os

import requests
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image as PILImage
from django.db import IntegrityError
from urllib3.util import parse_url

from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('places_dir', type=str)

    def handle(self, *args, **options):
        places_dir = options['places_dir']
        place_files = os.listdir(places_dir)
        media_dir = os.path.join(settings.BASE_DIR, 'media')
        os.makedirs(media_dir, exist_ok=True)

        for place_file in place_files:
            if place_file.endswith('.json'):
                with open(os.path.join(places_dir, place_file), encoding='utf8') as file:
                    place_obj = json.load(file)
                    place_title = place_obj['title']
                try:
                    place, _ = Place.objects.get_or_create(
                        title=place_title,
                        longitude=place_obj['coordinates']['lng'],
                        latitude=place_obj['coordinates']['lat'],
                        description_long=place_obj['description_long'],
                        description_short=place_obj['description_short'])
                except IntegrityError:
                    print(f'Skiped: {place_title}')
                    continue

                place_images_urls = place_obj['imgs']
                for number, image_url in enumerate(place_images_urls, start=1):
                    response = requests.get(image_url)
                    try:
                        response.raise_for_status()
                    except requests.exceptions.HTTPError:
                        continue

                    image_file_name = parse_url(image_url).path.split('/')[-1].lower()
                    image = Image(place=place, sequential_number=number)
                    try:
                        image.file.save(image_file_name, ContentFile(response.content), save=True)
                    except IntegrityError:
                        continue
                print(f'Done: {place_title}')
