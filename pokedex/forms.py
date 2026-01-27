from django import forms
from .models import Pokemon, Trainer

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': 'Nombre del Pokémon',
            'type': 'Tipo',
            'weight': 'Peso (kg)',
            'height': 'Altura (m)',
            'picture': 'Imagen del Pokémon',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Pikachu'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Eléctrico'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), # Ajusté el step
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'age': 'Edad',
            'date_of_birth': 'Fecha de Nacimiento',
            'level': 'Nivel',
            'picture': 'Foto del Entrenador', # Agregamos la etiqueta
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}), # Agregamos el widget para subir archivos
        }