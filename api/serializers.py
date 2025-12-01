from rest_framework import serializers
from pokedex.models import Pokemon, Trainer

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

class EntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'