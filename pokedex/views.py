from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import PokemonForm, EntrenadorForm 
from .models import Pokemon, Trainer
from rest_framework import viewsets, permissions
from .serializers import TrainerSerializer

# --- API PARA REACT ---
class TrainerAPIViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    # Esto debe estar dentro de la clase (con sangría)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# --- VISTAS PÚBLICAS ---
def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons, 'trainers': trainers})

def pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_list.html', {'trainers': trainers})

def display_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    return render(request, 'display_trainer.html', {'trainer': trainer})

# --- VISTAS PRIVADAS: POKÉMON ---
@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
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

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')

# --- VISTAS PRIVADAS: ENTRENADORES ---
@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers') # Redirige a la lista
    else:
        form = EntrenadorForm()
    # Este return es vital para evitar el ValueError
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers')
    else:
        form = EntrenadorForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    trainer.delete()
    return redirect('pokedex:trainers')

# --- AUTENTICACIÓN ---
class CustomLoginView(LoginView):
    template_name = 'login_form.html'