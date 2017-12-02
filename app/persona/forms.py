from django import forms
from app.persona.models import Estudiante,Asesor,Directivo

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante

        fields = [
            'nombre',
            'primer_apellido',
            'segundo_apellido',
            'cedula',
            'usuario',
            'tipo_usuario',
            'area',

        ]
        labels = {
            'nombre': 'Nombre',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'cedula': 'Cedula',
            'usuario': 'Usuario',
            'tipo_usuario': 'Tipo Usuario',
            'area': 'Área',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class':'form-control'}),
            'area': forms.Select(attrs={'class':'form-control'}),

        }
class AsesorForm(forms.ModelForm):
    class Meta:
        model = Asesor

        fields = [
            'nombre',
            'primer_apellido',
            'segundo_apellido',
            'cedula',
            'usuario',
            'tipo_usuario',
            'grupo_investigacion',
        ]
        labels = {
            'nombre': 'Nombre',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'cedula': 'Cedula',
            'usuario': 'Usuario',
            'tipo_usuario': 'Tipo Usuario',
            'grupo_investigacion': 'Grupo Investigacion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
            'grupo_investigacion': forms.Select(attrs={'class':'form-control'}),
        }
class DirectivoForm(forms.ModelForm):
    class Meta:
        model = Directivo

        fields = [
            'nombre',
            'primer_apellido',
            'segundo_apellido',
            'cedula',
            'usuario',
            'tipo_usuario',
            'cargo',
        ]
        labels = {
            'nombre': 'Nombre',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'cedula': 'Cedula',
            'usuario': 'Usuario',
            'tipo_usuario': 'Tipo Usuario',
            'cargo': 'Cargo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class':'form-control'}),
        }