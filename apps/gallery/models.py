from django.utils.translation import gettext_lazy as _
from django.db import models


class GalleryItem(models.Model):
    item_title = models.CharField(max_length=150)
    image = models.ImageField()
