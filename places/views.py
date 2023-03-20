from django.shortcuts import render

from places.models import Place
from where_to_go.settings import STATIC_URL


def index(request):
    places = Place.objects.all().iterator()
    places_geojson = {"type": "FeatureCollection", "features": []}
    for place in places:
        places_geojson["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"{STATIC_URL}places/moscow_legends.json"}})
    return render(request, "index.html", context={"places_geojson": places_geojson})
