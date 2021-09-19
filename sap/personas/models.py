from django.db import models

# Create your models here.
# Aqui se crea el modelo de las tablas a crearse en la base de datos, y después se hace la migración
#Primero se ponen las clases de tablas que no estan relacionadas con otras
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f"Domicilio: {self.id}. {self.calle} {self.no_calle}, {self.pais}"

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True, default=None, blank=False)

    def __str__(self):
        return f"Persona {self.id}, {self.nombre} {self.apellido} {self.email} {self.domicilio}"

