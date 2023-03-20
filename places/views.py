
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all().iterator()
    places_geojson = {"type": "FeatureCollection", "features": []}
    for place in places:
        places_geojson["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(place_details, kwargs={"place_id": place.id})
                }
            }
        )
    return render(request, "index.html", context={"places_geojson": places_geojson})


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    data = {
        "title": place.title,
        "imgs": [image.absolute_url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
