from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from pokedex.forms import PokemonForm
from django.shortcuts import redirect, render, get_object_or_404

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    context = {
        'pokemons': pokemons,
        'trainers': trainers,
    }
    return HttpResponse(template.render(context, request))

def pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def display_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

# --- CRUD for Pokemon ---

def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

def edit_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})

def delete_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    # Nota: para una confirmación podrías mostrar una plantilla; aquí se borra directamente.
    pokemon.delete()
    return redirect('pokedex:index')
