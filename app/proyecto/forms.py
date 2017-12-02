from django import forms
from django.forms import ClearableFileInput
from app.proyecto.models import ProyectoGrado

class CustomClearableFileInput(ClearableFileInput):
    #template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
    template_with_clear = ''

class ProyectoForm(forms.ModelForm):

    class Meta:
        model = ProyectoGrado

        fields = [
            'nombre',
            'fecha_incripcion',
            'alumno',
            'profesor',
            'area',
            'comentario',
            'correo_alumno',
            'correo_profesor',
            'archivo',
            'nota1',
            'nota2',
            'nota3',
            'nota4',
        ]
        labels = {
            'nombre': 'Nombre',
            'fecha_incripcion': 'Fecha Incripcion',
            'alumno': 'Alumno',
            'profesor': 'Profesor',
            'area': 'Area',
            'comentario': 'Comentario',
            'correo_alumno': 'Correo Alumno',
            'correo_profesor': 'Correo Profesor',
            'archivo': 'Archivo',
            'nota1': 'Nota 01',
            'nota2': 'Nota 02',
            'nota3': 'Nota 03',
            'nota4': 'Nota 04',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            #'fecha_incripcion':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_incripcion': forms.SelectDateWidget(attrs={'class':'form-control'}),
            #'fecha_incripcion': forms.DateInput(format='%d/%m/%y'),
            'alumno':forms.Select(attrs={'class':'form-control'}),
            'profesor':forms.Select(attrs={'class':'form-control'}),
            'area':forms.Select(attrs={'class':'form-control'}),
            'comentario':forms.Textarea(attrs={'class':'form-control'}),
            'correo_alumno': forms.EmailInput(attrs={'class':'form-control'}),
            'correo_profesor': forms.EmailInput(attrs={'class':'form-control'}),
            'archivo': ClearableFileInput,
            'nota1': forms.TextInput(attrs={'class': 'form-control'}),
            'nota2': forms.TextInput(attrs={'class': 'form-control'}),
            'nota3': forms.TextInput(attrs={'class': 'form-control'}),
            'nota4': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ProyectoForm2(forms.ModelForm):

    class Meta:
        model = ProyectoGrado

        fields = [
            'archivo',
        ]
        labels = {
            'archivo': 'Archivo',
        }
        widgets = {
            'archivo': ClearableFileInput,

        }

class ProyectoForm3(forms.ModelForm):

    class Meta:
        model = ProyectoGrado

        fields = [
            'comentario',
            'archivo',
            'nota1',
            'nota2',
            'nota3',
            'nota4',

        ]
        labels = {
            'comentario': 'Comentario',
            'archivo': 'Archivo',
            'nota1': 'Nota 01',
            'nota2': 'Nota 02',
            'nota3': 'Nota 03',
            'nota4': 'Nota 04',
        }
        widgets = {
            'comentario':forms.Textarea(attrs={'class':'form-control'}),
            'archivo': ClearableFileInput,
            'nota1': forms.TextInput(attrs={'class': 'form-control'}),
            'nota2': forms.TextInput(attrs={'class': 'form-control'}),
            'nota3': forms.TextInput(attrs={'class': 'form-control'}),
            'nota4': forms.TextInput(attrs={'class': 'form-control'}),

        }
