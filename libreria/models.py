from django.db import models

# Create your models here.
class libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Image', null=True)
    descripcion = models.TextField(verbose_name='Desripcion', null=True)
