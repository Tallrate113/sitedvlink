from django.conf.urls.static import static
from django.urls import path

from sitedvlink import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('account/', account, name='account'),
    path('signin/', signin, name='signin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
