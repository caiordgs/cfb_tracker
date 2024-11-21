from django import forms
from .models import Stat

class StatForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = '__all__'  # Inclui todos os campos do modelo
        widgets = {
            'season': forms.TextInput(attrs={'placeholder': 'Ano da temporada'}),
            'player': forms.Select(attrs={'class': 'form-control'}),
        }
