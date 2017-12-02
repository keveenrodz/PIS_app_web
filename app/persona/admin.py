from django.contrib import admin
from app.persona.models import Estudiante,Asesor,Persona,Directivo
# Register your models here.

admin.site.register(Persona)
admin.site.register(Asesor)
admin.site.register(Estudiante)
admin.site.register(Directivo)
