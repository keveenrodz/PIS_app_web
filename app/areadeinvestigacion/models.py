from django.db import models

# Create your models here.

class area(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class GrupoInvestigacion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:         #####################Evita que django "cite en plural"
        verbose_name_plural = "Grupos Investigacion"
