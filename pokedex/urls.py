"""
URL configuration for pokedex app.
"""
from django.urls import path
from . import views  # Importa las vistas de tu app

urlpatterns = [
    # Estas son las URLs de tu app
    path("", views.index, name="index"),
    path("trainer/<int:id>/", views.display_trainer, name="display_trainer"),
    path("<int:id>/", views.pokemon, name="pokemon"),
]