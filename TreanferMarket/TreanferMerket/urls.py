from django.urls import path, include
from .views import *

urlpatterns = [
    path('info', info_view, name='info_view'),
    path('index', index_view, name='index_view'),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Для медиа-файлов
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
