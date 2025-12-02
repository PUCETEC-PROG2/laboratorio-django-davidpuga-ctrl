# api/serializers.py
from rest_framework import serializers
from django.apps import apps

Pokemon = apps.get_model('pokedex', 'Pokemon')
Trainer = apps.get_model('pokedex', 'Trainer')


class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"
