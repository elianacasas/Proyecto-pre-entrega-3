from django.db import models

# Create your models here.
class Velero(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    password = models.IntegerField()
    firs_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth =models.DateField()


class Band_members(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    date_of_join = models.DateField()
    instrument = models.CharField(max_length=20)
    
class Albums(models.Model):
    name = models.CharField(max_length=20)
    date_of_record = models.DateField()
    
