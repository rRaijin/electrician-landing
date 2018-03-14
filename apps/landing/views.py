from django.views.generic import TemplateView

from apps.advantages.models import Advantage
from apps.gallery.models import GalleryItem
from apps.landing.forms import TelegrammForm
from apps.skills.models import Skill


class MainPage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advantages'] = Advantage.objects.all()[:3]
        context['skills'] = Skill.objects.all()
        context['gallery'] = GalleryItem.objects.all()
        context['TelegrammForm'] = TelegrammForm()
        return context
