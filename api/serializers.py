# api/serializers.py
from rest_framework import serializers
from django.apps import apps

Pokemon = apps.get_model('pokedex', 'Pokemon')
Trainer = apps.get_model('pokedex', 'Trainer')


class PokemonSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(required=False)

    class Meta:
        model = Pokemon
        fields = "__all__"

    def create(self, validated_data):
        picture_name = validated_data.pop("picture", None)

        pokemon = Pokemon.objects.create(**validated_data)

        if picture_name:
            pokemon.picture.name = f"pokemon_picture/{picture_name}"
            pokemon.save()

        return pokemon


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"
