from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', MainPage.as_view(), name='main'),
]