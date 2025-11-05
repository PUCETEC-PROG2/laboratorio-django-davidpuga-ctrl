from django import forms
from .models import Pokemon

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
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.0001'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.0001'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }
