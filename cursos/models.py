from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_horas = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    cupo_maximo = models.PositiveSmallIntegerField()
    nivel = models.CharField(
        max_length=50,
        choices=[('Básico', 'Básico'), ('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado')]
    )
    imagen = models.ImageField(upload_to='media/fotos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
class Meta:
    verbose_name = "Curso"
    verbose_name_plural = "Cursos"
    ordering = ['fecha_creacion']

