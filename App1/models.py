from django.db import models

# Create your models here.
class Suscriptos(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    password = models.IntegerField()
    firs_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth =models.DateField()


class Historias(models.Model):
    name = models.CharField(max_length=20)
    opinion = models.CharField(max_length=200)
    date = models.DateField()
    
    
class Playlist(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    link = models.URLField()
    
