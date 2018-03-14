from django.conf.urls import url

from apps.advantages.views import EditAdvantage


urlpatterns = [
    url(r'^(?P<id>\d+)/edit/$', EditAdvantage.as_view(), name='edit'),
]