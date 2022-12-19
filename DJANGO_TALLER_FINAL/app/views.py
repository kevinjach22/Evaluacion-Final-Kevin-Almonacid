from django.shortcuts import render, redirect
from .models import Inscrito, Institucion
from .forms import FormInscritos

from django.http import JsonResponse

from .serialiazers import InscritoSerializer, InstitucionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return render(request, 'index.html')

def crud(request):
    return render(request, 'crud.html')

def lista_inscrito(request):
    inscritos = Inscrito.objects.all()
    data = {'inscritos': inscritos}
    return render(request, 'listar_inscrito.html', data)

def agrega_inscrito(request):
    form = FormInscritos()
    if request.method == 'POST':
        print(request.POST)
        form = FormInscritos(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_inscrito.html', data)

def elimina_inscrito(request, id):
    inscrito = Inscrito.objects.get(id = id)
    inscrito.delete()
    return redirect('/crud/listar_inscrito')

def actualiza_inscrito(request, id):
    inscrito_actualizado = Inscrito.objects.get(id = id)
    form = FormInscritos(instance=inscrito_actualizado)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=inscrito_actualizado)
        if form.is_valid() :
            form.save()
        return redirect('/crud/listar_inscrito')
    data = {'form' : form}
    return render(request, 'actualizar_inscrito.html', data)

#API
def verinscritoDb(request):
    inscrito = Inscrito.objects.all()
    data = {'inscrito' : list(inscrito.values('nombre','telefono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion'))}

    return JsonResponse(data)


#CBW
class ListarInscrito(APIView):

    def get(self, request):
        inscri = Inscrito.objects.all()
        serial = InscritoSerializer(inscri, many=True)
        return Response(serial.data)
    
class DetalleInscrito(APIView):

    def get_object(self, pk):
        try:
            return Inscrito.objects.get(pk=pk)
        except Inscrito.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        inscri = self.get_object(pk)
        serial = InscritoSerializer(inscri)
        return Response(serial.data)

#FBW
@api_view(['GET'])
def institucion_list(request):
    if request.method == 'GET':
        insti = Institucion.objects.all()
        serial = InstitucionSerializer(insti, many=True)
        return Response(serial.data)

@api_view(['GET'])
def institucion_detalle(request, pk):
    try:
        insti = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(insti)
        return Response(serial.data)

