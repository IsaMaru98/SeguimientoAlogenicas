from django.shortcuts import render, HttpResponse

from .models import Cosecha
# Create your views here.

## en esta función llamo los datos de Cosecha con el objects.all() y estos los paso por medio de un diccionario al html 
# en el archivo html puedo mostrar estos datos del objeto usando un ciclo for 

def home(request): 
    datosCosecha = Cosecha.objects.all()
    return render(request, 'formularios/home.html', {'datosCosecha': datosCosecha} )
