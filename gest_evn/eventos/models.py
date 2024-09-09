from django.db import models

class Organizador(models.Model):
    nombre = models.CharField(max_length=30)

class Evento(models.Model):
    nombre = models.CharField(max_length=30)
    Organizador= models.ForeignKey(Organizador, on_delete=models.CASCADE)
    fecha =  models.DateField()



