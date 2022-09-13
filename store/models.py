from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.html import format_html
import time

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField()
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateTimeField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre


opciones_consultas =[
    [0, "consultas"],
    [1, "reclamos"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]
        
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
    
    
class Datosusuario(models.Model):
    usuario              = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", default='defecto/defecto.png', blank=True, null=True) 
    nombre               = models.CharField(max_length=50)
    apellido             = models.CharField(max_length=50)
    fecha_nacimiento     = models.DateField(blank=True, null=True)
    pais                 = models.CharField(max_length=30, blank=True)
    provincia            = models.CharField(max_length=40, blank=True)
    ciudad               = models.CharField(max_length=40, blank=True)
    domicilio            = models.CharField(max_length=80, blank=True)
    codigo_postal        = models.CharField(max_length=50, blank=True)
    telefono             = models.CharField(max_length=30, blank=True)
    celular              = models.CharField(max_length=30, blank=True)
    documento            = models.CharField(max_length=30, blank=True)
    cuit                 = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return self.usuario.username




# Create your models here.
