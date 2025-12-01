from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from pokedex.models import Pokemon , Trainer
from .serializers import PokemonSerializer , EntrenadorSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class=  PokemonSerializer
    required_scopes=['write']

class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = EntrenadorSerializer