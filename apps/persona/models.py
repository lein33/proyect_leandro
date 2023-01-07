from django.db import models

class Persona(models.Model):
    genero = (('Femenino','Femenino'),('Masculino','Masculino'))
    dni = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=8)
    edad = models.IntegerField(blank=True)
    sexo = models.CharField(max_length=10,choices=genero,default='F')
    correo = models.CharField(max_length=25)
    pais = models.CharField(max_length=15)
    provincia = models.CharField(max_length=15)
    direccion = models.CharField(max_length=25)
    cod_postal = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.nombre}'