from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=15)
    curso = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
