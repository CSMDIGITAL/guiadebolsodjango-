from django import forms
from .models import Associado

class AssociadoForm(forms.ModelForm):
    class Meta:
        model = Associado
        fields = ['nome', 'email', 'telefone', 'foto', 'status', 'matricula', 'cargo', 'empresa']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
        }