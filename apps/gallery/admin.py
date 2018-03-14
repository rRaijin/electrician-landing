from django.contrib import admin
from .models import GalleryItem


class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_title']

    class Meta:
        model: GalleryItem

admin.site.register(GalleryItem, GalleryItemAdmin)