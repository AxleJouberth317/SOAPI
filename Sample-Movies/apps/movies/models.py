from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Planes(models.Model):
    tipoplan = models.CharField(max_length=30)
    valor = models.IntegerField()

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=60)
    paisnac = models.CharField(max_length=30)
    tipoplan = models.ForeignKey(Planes, null=True, blank=True, on_delete=models.CASCADE)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    reparto = models.CharField(max_length=300)
    tipoplan = models.ForeignKey(Planes, null=True, blank=True, on_delete=models.CASCADE)

class Registro(models.Model):
    cliente = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, null=True, blank=True, on_delete=models.CASCADE)
    calificacion = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
    fecha = models.DateField()
    hora = models.TimeField()

