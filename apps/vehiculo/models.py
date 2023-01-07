from django.db import models
from apps.persona.models import Persona

class Mantenimiento(models.Model):
    id_mate = models.AutoField(primary_key=True)
    descipcion = models.CharField(max_length=85)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.descipcion}'


class Vehiculo(models.Model):
    placa = models.CharField(max_length=8, primary_key=True)
    marca = models.CharField(max_length=65)
    modelo = models.CharField(max_length=65)
    tipo = models.CharField(max_length=45)
    color = models.CharField(max_length=65)
    cc = models.IntegerField(blank=True, null=False)
    persona = models.ForeignKey(Persona, null=True, on_delete=models.CASCADE)
    mantenimiento = models.ManyToManyField(Mantenimiento, blank=True)
