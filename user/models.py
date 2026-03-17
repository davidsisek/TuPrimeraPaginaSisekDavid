from django.db import models

# Create your models here.

class Toldos(models.Model):
    cliente = models.CharField(max_length=50)
    tipo_toldo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.cliente} ({self.tipo_toldo})"


class RopaTrabajo(models.Model):
    nombre = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nombre} (Talle: {self.talle})" 

class ArtCamping(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.nombre
