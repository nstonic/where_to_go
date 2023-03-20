from django.contrib import admin

from places.models import Place, Image


class ImagesInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('file', 'preview', 'sequential_number')
    readonly_fields = ["preview"]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ["title"]
    inlines = [ImagesInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
