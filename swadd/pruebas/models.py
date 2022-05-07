from secrets import choice
from django.db import models

# Create your models here.
class Prueba(models.Model):
    sexo_eleccion = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    
    estado_civil_eleccion = (
        ( 'S','Soltero'),
        ('C','Casado'),
        ('V','Viudo'),
        ('D','Divorciado'),
        ('Co','Conviviente')
    )
        
    
    nombre_completo = models.CharField(max_length=300)
    estado_civil = models.CharField(choices=estado_civil_eleccion, max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(choices=sexo_eleccion,max_length=100)
    ocupacion = models.CharField(max_length=200)
    educacion = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
    pregunta01 = models.IntegerField()
    pregunta02 = models.IntegerField()
    pregunta03 = models.IntegerField()
    pregunta04 = models.IntegerField()
    pregunta05 = models.IntegerField()
    pregunta06 = models.IntegerField()
    pregunta07 = models.IntegerField()
    pregunta08 = models.IntegerField()
    pregunta09 = models.IntegerField()
    pregunta10 = models.IntegerField()
    pregunta11 = models.IntegerField()
    pregunta12 = models.IntegerField()
    pregunta13 = models.IntegerField()
    pregunta14 = models.IntegerField()
    pregunta15 = models.IntegerField()
    pregunta16 = models.IntegerField()
    pregunta17 = models.IntegerField()
    pregunta18 = models.IntegerField()
    pregunta19 = models.IntegerField()
    pregunta20 = models.IntegerField()
    pregunta21 = models.IntegerField()
    total = models.IntegerField()
    resultado_test = models.CharField(max_length=500, blank=True)
    estado_animico = models.CharField(max_length=800,blank=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/',blank=True)
    slug = models.CharField(max_length=200, blank=True, unique=True)
    
    def __str__(self) -> str:
        return self.nombre_completo