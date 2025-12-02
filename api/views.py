from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ['write']  


class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = EntrenadorSerializer

    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            permission_classes = [IsAuthenticated, TokenHasScope]
        else:
            permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
        
        return [permission() for permission in permission_classes]
