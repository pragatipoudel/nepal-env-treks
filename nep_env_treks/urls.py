
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('', include('homepage.urls')),
    path('packages/', include('packages.urls', namespace='packages')),
    path('inquiries/', include('inquiries.urls', namespace='inquiries')),
    path('information/', include('information.urls', namespace='information')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
