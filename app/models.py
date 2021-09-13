from django.db import models


class Sintoma(models.Model):
    simbolo = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Diagnostico(models.Model):
    simbolo = models.CharField(max_length=50, unique=True)
    resultado = models.CharField(max_length=150)
    sintomas = models.ManyToManyField(Sintoma)

    def __str__(self):
        return self.resultado


class diagnosticoUsuario(models.Model):
    name = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    age = models.IntegerField()
    genre = models.CharField(max_length=1)
