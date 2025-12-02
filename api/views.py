from rest_framework import viewsets
from django.apps import apps
from .serializers import PokemonSerializer, TrainerSerializer

Pokemon = apps.get_model('pokedex', 'Pokemon')
Trainer = apps.get_model('pokedex', 'Trainer')


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
