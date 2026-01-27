from django.shortcuts import render
from rest_framework import viewsets
# Importamos explícitamente todos los permisos necesarios
from rest_framework.permissions import IsAuthenticated, AllowAny # <--- Añadido AllowAny
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope, 
    TokenHasScope, 
    OAuth2Authentication
)

from pokedex.models import Pokemon, Trainer
from .serializers import PokemonSerializer, EntrenadorSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    authentication_classes = [OAuth2Authentication]
    # No definimos permission_classes globalmente, lo manejamos en el método:
    # permission_classes = [IsAuthenticated, TokenHasScope] <-- ELIMINADO
    required_scopes = ['write']  

    # Permisos para PokemonViewSet (Lectura abierta, Escritura con token)
    def get_permissions(self):
        # Para POST, PUT, PATCH, DELETE (modificación), exigimos autenticación
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [TokenHasScope(), IsAuthenticated()]
        
        # Para GET, HEAD, OPTIONS (lectura), permitimos a cualquiera
        return [AllowAny()] # <--- ¡SOLUCIÓN PARA QUE REACT VEA LA LISTA!


class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = EntrenadorSerializer

    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']

    # Permisos para EntrenadorViewSet (Corregimos la lógica para que no falle)
    def get_permissions(self):
        # Si tienes TokenHasReadWriteScope, debes asegurarte de que esté importado
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            # La lectura también requiere autenticación y scope aquí, si eso es lo que deseas
            return [IsAuthenticated(), TokenHasScope()] 
        else:
            # Para escritura, usa el scope completo (TokenHasReadWriteScope)
            return [IsAuthenticated(), TokenHasReadWriteScope()]