from django.db import models
from app.persona.models import Estudiante, Asesor
from app.areadeinvestigacion.models import area
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class ProyectoGrado(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_incripcion = models.DateField()
    alumno = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    correo_alumno= models.CharField(max_length=50,null=True, blank=False)
    correo_profesor= models.CharField(max_length=50,null=True, blank=False)
    profesor = models.ForeignKey(Asesor, null=False, blank=False, on_delete=models.CASCADE)
    area = models.ForeignKey(area, null=False, blank=False, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=150,null=True, blank=True)
    archivo = models.FileField(upload_to="archivos/", null=True, blank=True)
    nota1 = models.FloatField(null=True, blank=True,validators=[MinValueValidator(0.0), MaxValueValidator(5.0)] )
    nota2 = models.FloatField(null=True, blank=True,validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    nota3 = models.FloatField(null=True, blank=True,validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    nota4 = models.FloatField(null=True, blank=True,validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def nombreproy(self):  ####################Devolver el nombre completo
        cadena = 'Nombre:{0}, | Alumno: {1} |, | Asesor:{2} |, |Area:{3}|'
        return cadena.format(self.nombre,self.alumno,self.profesor,self.area)

    def __str__(self):  ######################Mostrar en el servidor el nombre completo
        return self.nombreproy()

    class Meta:         #####################Evita que django "cite en plural"
        verbose_name_plural = "Proyecto Grado"

