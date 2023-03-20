from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.contrib import admin

from places.models import Place, Image


class ImagesInline(SortableStackedInline):
    model = Image
    extra = 1
    fields = ('file', 'preview', 'sequential_number')
    readonly_fields = ["preview"]


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ["title"]
    inlines = [ImagesInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
