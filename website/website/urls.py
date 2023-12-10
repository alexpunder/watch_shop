from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


handler403 = 'util_pages.views.page_forbidden'
handler404 = 'util_pages.views.page_not_found'
handler500 = 'util_pages.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('util_pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
