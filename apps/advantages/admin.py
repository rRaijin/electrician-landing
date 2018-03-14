from django.contrib import admin
from .models import Advantage


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']

    class Meta:
        model: Advantage

admin.site.register(Advantage, AdvantageAdmin)