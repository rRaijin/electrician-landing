from django.utils.translation import gettext_lazy as _
from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()

    class Meta:
        verbose_name = _('Skills')
        verbose_name_plural = _('Skill')
