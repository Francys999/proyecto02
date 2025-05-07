from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),        # vistas web
    path('api/', include('core.urls')),    # endpoints DRF (más adelante)
]
