from django import forms
from app.areadeinvestigacion.models import GrupoInvestigacion,area

class AreaForm(forms.ModelForm):
    class Meta:
        model = area

        fields = [
            'nombre'
        ]
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
         }


class GruposInvForm(forms.ModelForm):
    class Meta:
        model = GrupoInvestigacion

        fields = [
            'nombre'
        ]
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }