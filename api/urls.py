from django.urls import path, include
from rest_framework import routers
from . import views

# 1. Creamos el router una sola vez
router = routers.DefaultRouter()

# 2. Registramos TODOS los modelos en ese mismo router
router.register(r'pokemons', views.PokemonViewSet)
router.register(r'entrenadores', views.EntrenadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]