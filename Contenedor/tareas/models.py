from django.db import models

class Tarea(models.Model):
    nombre=models.CharField(max_length=255, unique=True)
    descripcion=models.TextField(max_length=4000)
    fecha_creacion=models.DateField(auto_now_add=True)
    fecha_actualizacion=models.DateField(auto_now=True)
    fecha_vencimiento=models.DateField(null=True, blank=True
                                )
    completada=models.BooleanField(default=True)
    