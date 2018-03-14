from django.utils.translation import gettext_lazy as _
from django.db import models


class Advantage(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    text = models.TextField()

    def get_short_text(self):
        return self.text[:80]

    class Meta:
        verbose_name = _('Advantages')
        verbose_name_plural = _('Advantage')
