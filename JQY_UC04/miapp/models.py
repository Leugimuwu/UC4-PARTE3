from django.db import models

# Create your models here.

#creamos modelo de estudiante
class Estudiante(models.Model):
    codigo = models.TextField(max_length=10)
    dni = models.TextField(max_length=8)
    nombre = models.TextField()
    apepat = models.TextField()
    apemat = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    estado = models.CharField(max_length=1)