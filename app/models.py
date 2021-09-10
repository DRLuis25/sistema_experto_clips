from django.db import models


class diagnostico(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    age = models.IntegerField()
    genre = models.CharField(max_length=1)
    diagnostic = models.CharField(max_length=150)
