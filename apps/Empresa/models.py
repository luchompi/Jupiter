from django.db import models


class Sede(models.Model):
    """Django data model Sede"""
    sede = models.CharField(max_length=50,verbose_name="Ingrese Nombre de la Sede",unique=True,error_messages={'unique':'Ya existe un registro con este nombre'})
    timestamps = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.sede)


class Dependencia(models.Model):
    """Django data model Dependencia"""
    dependencia = models.CharField(max_length=50,verbose_name="Ingrese nombre de la Dependencia",unique=True,error_messages={'unique':'Ya existe un registro con este nombre'})
    timestamps  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.dependencia)


class SedeDependencia(models.Model):
    sede =models.ForeignKey(Sede,on_delete=models.CASCADE)
    dependencia=models.ForeignKey(Dependencia,on_delete=models.CASCADE)
    timestamps = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.sede, self.dependencia)

