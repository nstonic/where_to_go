from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image

admin.site.register(Image)


class ImagesInline(SortableStackedInline):
    model = Image
    extra = 1
    fields = ('file', 'preview', 'sequential_number')
    readonly_fields = ['preview']

    def preview(self, image):
        return format_html(
            '<img src="{}" height="200" width="auto" />',
            image.file.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title']
    inlines = [ImagesInline]
