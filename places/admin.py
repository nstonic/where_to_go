from django.contrib import admin

from places.models import Place, Image


class ImagesInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title']
    inlines = [ImagesInline]


admin.site.register(Image)
