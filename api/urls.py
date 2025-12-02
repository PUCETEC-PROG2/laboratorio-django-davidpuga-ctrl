# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, TrainerViewSet   # <-- importa TrainerViewSet

router = DefaultRouter()
router.register(r'pokemons', PokemonViewSet)
router.register(r'trainers', TrainerViewSet)        # <-- NO entrenadores

urlpatterns = [
    path('', include(router.urls)),
]
