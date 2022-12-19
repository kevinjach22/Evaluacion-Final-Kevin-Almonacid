from dataclasses import fields
from socket import fromshare
from django import forms
from app.models import Inscrito

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = '__all__'
    
    fecha_inscripcion = forms.DateField(label="Fecha de inscripción", widget=forms.SelectDateWidget)
    hora_inscripcion = forms.TimeField(label="Hora de inscripción", widget=forms.TimeInput(attrs={'type':'time'}))
