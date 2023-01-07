from django.db import models
class pbv(models.Model):
    idpbv = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    cc = models.IntegerField()
    especificaciones = models.CharField(max_length=15)
