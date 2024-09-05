from django.db import models



class Evento(models.Model):
    nombre = models.CharField(max_length=30)
    Organizador= models.ForeignKey(Organizador)
    fecha =  model.DateField()

class Organizador(models.Model):
    nombre = models.CharField(max_length=30)

