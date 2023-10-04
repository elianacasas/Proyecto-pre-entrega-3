from django.db import models


# Create your models here.
class Suscriptos(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    password = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    

class Cafeterias(models.Model):
    name = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    horario = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    
    
class Reseñas(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    opinion = models.CharField(max_length=200)
    puntaje = models.IntegerField()
    
