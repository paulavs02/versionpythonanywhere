from django.db import models

# Create your models here.
class Project(models.Model):
    escuadra = models.CharField(max_length=200)
    players = models.TextField( verbose_name = "Integrantes")
    avatar = models.ImageField(upload_to="projects")
    kills = models.IntegerField(default=0,  verbose_name = "Bajas")
    points = models.DecimalField(max_digits=5, decimal_places=2,  verbose_name = "Puntos")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.escuadra
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        
    
  