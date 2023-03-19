from django.contrib import admin

from places.models import Place, Coordinates


@admin.register(Place)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title']


@admin.register(Coordinates)
class PostAdmin(admin.ModelAdmin):
    list_display = ['place', 'longitude', 'latitude']
