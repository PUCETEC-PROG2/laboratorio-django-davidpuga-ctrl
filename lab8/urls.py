"""
URL configuration for lab8 project. 
(El resto de la descripción está bien)
"""
from django.contrib import admin
from django.urls import path, include

# --- ¡Importa esto! ---
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea le dice a Django que busque las URLs de tu app
    path('', include('pokedex.urls')) # He quitado 'pokedex/' para que sea la página principal
]

# --- ¡Esta es la parte clave! ---
# Añade esta configuración al FINAL del archivo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)