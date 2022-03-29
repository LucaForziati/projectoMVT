from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre = models.CharField("nombre", max_length = 50)
    apellido = models.CharField("apellido", max_length = 50)
    num_de_la_suerte = models.IntegerField("num_de_la_suerte")
    nacimiento = models.DateField("nacimiento", max_length = 50)