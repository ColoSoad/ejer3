from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    fecha_nac = models.DateField()
    email = models.EmailField()

