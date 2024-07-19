from django.db import models
from pathlib import Path
from django.contrib.auth.models import User

#____ Plantas
class Plantas(models.Model):
    nombre = models.CharField(max_length=50)
    image = models.CharField(max_length=50)

    def __str__ (self):
        return f"{self.nombre}, {self.image}"

    class Meta:
        verbose_name = 'Plantas'
        verbose_name_plural = 'Plantas'

#____ Jardines
class Jardines(models.Model):
    nombre = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__ (self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = 'Jardines'
        verbose_name_plural = 'Jardines'

#____ Cultivos
class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    image = models.CharField(max_length=50)

    def __str__ (self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = 'Cultivos'
        verbose_name_plural = 'Cultivos'

class Reproduccion (models.Model):
    nombre = models.CharField(max_length=50)
    paso_numero = models.IntegerField()
    paso_nombre = models.CharField(max_length=50)
    paso_descripcion = models.CharField(max_length=1000)
    paso_image = models.CharField(max_length=50)

    def __str__ (self):
        return f"{self.nombre} {self.paso_numero} {self.paso_nombre}"

    class Meta:
        verbose_name = 'Reproducción'
        verbose_name_plural = 'Reproducción'
        ordering = ["nombre","paso_numero"]

class Contactos(models.Model):
    apellido = models.CharField(max_length=50)
    ciudad   = models.CharField(max_length=50)
    pais     = models.CharField(max_length=50)
    correo   = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    mensaje  = models.TextField(max_length=500)

    def __str__ (self):
        return f"{self.apellido}"

    class Meta:
        verbose_name = 'Contactos'
        verbose_name_plural = 'Contactos'

#____ Avatar
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__ (self):
        return f"{self.user} {self.imagen}"
