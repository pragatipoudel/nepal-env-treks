
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('', include('homepage.urls')),
    path('packages/', include('packages.urls', namespace='packages')),
    path('admin/', admin.site.urls),
    path('inquiry/', include('inquiries.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
