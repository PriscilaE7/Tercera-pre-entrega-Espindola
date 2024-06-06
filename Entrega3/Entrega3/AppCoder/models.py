from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Recetas(models.Model):

    nombre= models.CharField(max_length=30)
    ingredientes= models.IntegerField()
    def __str__(self):
        return f'{self.nombre} - {self.ingredientes}'

class Comentario(models.Model):
    nombre_de_usuario = models.TextField()
    apellido_de_usuario = models.TextField()
    comentario = models.TextField()
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.nombre} - {self.email} - {self.telefono} - {self.mensaje}'