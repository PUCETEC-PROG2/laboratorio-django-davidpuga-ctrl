from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from oauth2_provider import urls as oauth2_urls

# 1. Configuración del Router para la API de React
router = DefaultRouter()
router.register(r'entrenadores', views.TrainerAPIViewSet, basename='entrenador-api')

app_name = 'pokedex'

urlpatterns = [
    # --- RUTA PARA LA API (React la usará como /pokedex/api/entrenadores/) ---
    path("api/", include(router.urls)), 

    # --- RUTAS DE NAVEGACIÓN HTML (Panel de Django) ---
    path("", views.index, name="index"),
    path("trainers/", views.trainer_list, name="trainers"),
    path("trainer/<int:id>/", views.display_trainer, name="display_trainer"),
    
    # --- CRUD ENTRENADORES (Formularios Django) ---
    path("add_trainer/", views.add_trainer, name="add_trainer"),
    path("edit_trainer/<int:id>/", views.edit_trainer, name="edit_trainer"),
    path("delete_trainer/<int:id>/", views.delete_trainer, name="delete_trainer"),
    
    # --- CRUD POKEMON (Formularios Django) ---
    path("<int:id>/", views.pokemon, name="pokemon"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    
    # --- CUENTAS ---
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('o/', include((oauth2_urls, 'oauth2_provider'), namespace='oauth2_provider')),
]