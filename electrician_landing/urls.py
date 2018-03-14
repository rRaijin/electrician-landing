"""
electrician_landing URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from electrician_landing import telegramm

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^feedback/', telegramm.handle, name='feedback'),
    url(r'^advantages/', include('apps.advantages.urls', namespace='advantages')),
    # url(r'^skills/', include('apps.skills.urls', namespace='skills')),
    url(r'^', include('apps.landing.urls', namespace='home')),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
