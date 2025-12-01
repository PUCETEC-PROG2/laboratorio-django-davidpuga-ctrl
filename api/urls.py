from django.urls import path, include
from rest_framework import routers
from . import views

# 1. Creamos el router una sola vez
router = routers.DefaultRouter()

# 2. Registramos TODOS los modelos en ese mismo router
router.register(r'pokemons', views.PokemonViewSet)
router.register(r'entrenadores', views.EntrenadorViewSet)

# 3. Definimos urlpatterns UNA sola vez al final
urlpatterns = [
    # Usamos cadena vacía '' porque el prefijo 'api/' ya está en el archivo principal (lab8/urls.py)
    path('', include(router.urls)),
]