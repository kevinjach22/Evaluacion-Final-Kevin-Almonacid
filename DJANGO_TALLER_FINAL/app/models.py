from django.db import models
# Create your models here.

opciones_estado = [
    [0, "Reservado"],
    [1, "Completada"],
    [2, "Anulada"],
    [3, "No Asiste"]
]

class Institucion(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    def __str__(self):
        return f'{self.nombre}'
    
class Inscrito(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    telefono = models.IntegerField(verbose_name="Teléfono")
    fecha_inscripcion = models.DateField(verbose_name="Fecha de inscripción")
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='inscrito')
    hora_inscripcion = models.TimeField(verbose_name="Hora de inscripción", auto_now=False, auto_now_add=False)
    estado = models.IntegerField(verbose_name="Estado", choices = opciones_estado)
    observacion = models.TextField(verbose_name="Observación", max_length=254)



