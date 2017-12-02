from django.db import models
from django.contrib.auth.models import User
from app.areadeinvestigacion.models import area, GrupoInvestigacion
from django.contrib.auth.models import User

# Create your models here.

RESULTADO_P = (
    ('Estudiante', 'Estudiante'),
    ('Asesor', 'Asesor'),
    ('Directivo', 'Directivo'),
)

class Persona(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    tipo_usuario = models.CharField(max_length=50, choices=RESULTADO_P)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    cedula = models.IntegerField()

    def nombreper(self):  ####################Devolver el nombre completo
        cadena = 'Usuario:{0}, Tipo: {1} , Nombre:{2} , Apellidos:{3} {4}'
        return cadena.format(self.usuario,self.tipo_usuario,self.nombre,self.primer_apellido,self.segundo_apellido)

    def __str__(self):  ######################Mostrar en el servidor el nombre completo
        return self.nombreper()


class Estudiante(Persona,models.Model):
    area = models.ForeignKey(area, null=False, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.primer_apellido, self.segundo_apellido)


class Asesor(Persona,models.Model):
    grupo_investigacion = models.ForeignKey(GrupoInvestigacion, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.primer_apellido, self.segundo_apellido)

class Directivo(Persona,models.Model):
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.primer_apellido, self.segundo_apellido)



