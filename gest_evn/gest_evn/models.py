
from django.db import models

class Organizador(models.Model):
    nombre = models.CharField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField()
    fecha = models.DateField()
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

