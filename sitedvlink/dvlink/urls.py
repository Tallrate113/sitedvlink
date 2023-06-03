from django.conf.urls.static import static
from django.urls import path, include

from sitedvlink import settings
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'application', ApplicationsViewSet, basename='applications')

urlpatterns = [
    path('', index, name='home'),
    path('account/', account, name='account'),
    path('signin/', signin, name='signin'),
    path('api/v1/', include(router.urls)),
    path('api/v1/dvlink-auth', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
