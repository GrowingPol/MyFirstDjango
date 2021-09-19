from django.db import models

# Create your models here.
# Aqui se crea el modelo de las tablas a crearse en la base de datos, y después se hace la migración
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)