from django.db import models

class Caminante(models.Model):
    nombre = models.CharField("Nombre", max_length=50, blank = False)
    correo = models.CharField("Correo", max_length=50, blank = False)
    Km_semanales = models.IntegerField(null=True)
