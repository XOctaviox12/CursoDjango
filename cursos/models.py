from django.db import models
from ckeditor.fields import RichTextField

from django.db import models

class Curso(models.Model):
    NIVELES = [
        ('B', 'Básico'),
        ('I', 'Intermedio'), 
        ('A', 'Avanzado')
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=1, choices=NIVELES, default='B')
    precio = models.DecimalField(max_digits=8, decimal_places=2,default=0.00)
    duracion = models.PositiveSmallIntegerField(help_text="Duración en horas",default=20)
    imagen = models.ImageField(upload_to='cursos/')
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} ({self.get_nivel_display()})"

class Actividad(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre_curso = models.ForeignKey(Curso,on_delete=models.CASCADE,verbose_name="Nombre curso")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    descripcion = RichTextField(verbose_name="Descripcion")

    class Meta:
            verbose_name = "Actividad"
            verbose_name_plural = "Actividad"
            ordering = ["-created"]

    def __str__(self):
        return str(self.nombre_curso)

