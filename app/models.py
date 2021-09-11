from django.db import models


class Sintoma(models.Model):
    simbolo = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100)

class Diagnostico(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    age = models.IntegerField()
    genre = models.CharField(max_length=1)
    diagnostic = models.CharField(max_length=150)