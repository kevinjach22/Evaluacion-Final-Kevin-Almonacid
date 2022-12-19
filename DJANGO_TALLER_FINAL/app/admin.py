from django.contrib import admin
from app.models import Inscrito

# Register your models here.

class InscritoAdmin(admin.ModelAdmin):
    list_display = ['nombre','telefono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion']

admin.site.register(Inscrito, InscritoAdmin)
