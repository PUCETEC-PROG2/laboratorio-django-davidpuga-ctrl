from rest_framework import viewsets
from django.apps import apps
from .serializers import PokemonSerializer, TrainerSerializer

from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope, 
    TokenHasScope # <-- Usa esta clase de permiso
)

from rest_framework.permissions import IsAuthenticated, AllowAny


Pokemon = apps.get_model('pokedex', 'Pokemon')
Trainer = apps.get_model('pokedex', 'Trainer')


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    # 1. 🚨 CAMBIO CLAVE: Define el atributo required_scopes
    # Si quieres permitir la lectura para todos, pero la escritura/edición/eliminación
    # solo para tokens con scope 'write'.
    required_scopes = ['write'] 

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # 2. Usa TokenHasScope sin paréntesis para que se evalúe correctamente en el ViewSet
            # La autenticación IsAuthenticated puede ser redundante si TokenHasScope lo requiere, 
            # pero es una buena práctica dejarlo para claridad.
            return [IsAuthenticated(), TokenHasScope()]
        
        # Para GET (lista o detalle) permitimos a cualquiera (sin token).
        return [AllowAny()] 


class TrainerViewSet(viewsets.ModelViewSet):
    # Aquí probablemente también querrías añadir required_scopes si usas TokenHasScope
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    required_scopes = ['write']
    
    def get_permissions(self):
        # Aplicamos la misma lógica para los Entrenadores
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), TokenHasScope()]
        return [AllowAny()]