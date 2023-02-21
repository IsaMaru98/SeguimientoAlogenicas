from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from . import models
from . import forms
# Create your views here.

## en esta función llamo los datos de Cosecha con el objects.all() y estos los paso por medio de un diccionario al html 
# en el archivo html puedo mostrar estos datos del objeto usando un ciclo for 
def home(request):
    return render(request, 'formularios/home.html', {})
def cosechaForm(request): 

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        formCosecha = forms.CosechaForm(request.POST)
        # check whether it's valid:
        if formCosecha.is_valid():

            formCosecha.save()
            # redirect to a new URL:
            return HttpResponse('<h1> Datos guardados </h1>')

    # if a GET (or any other method) we'll create a blank form
    else:
        formCosecha = forms.CosechaForm()
    
    return render(request, 'formularios/formularioCosecha.html', {'formCosecha': formCosecha} )

def siembraForm(request): 
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        formSiembra= forms.SiembraForm(request.POST)
        
        if formSiembra.is_valid():

            formSiembra.save()
            # redirect to a new URL:
    
            return HttpResponse('<h1> Datos guardados </h1>' )
    else:
        formSiembra = forms.SiembraForm()
    
    return render(request, 'formularios/formularioSiembra.html', {'formSiembra': formSiembra} )

def crioForm(request):

    if request.method == 'POST': 
        formCrio = forms.CrioForm(request.POST)
        if formCrio.is_valid():
            formCrio.save() 

            return HttpResponse('<h1> Datos guardados </h1>' )
    
    else:
        formCrio = forms.CrioForm()
    
    return render(request, 'formularios/formularioCrio.html', {'formCrio': formCrio} )

def datos(request): 
    datosCosecha = models.Cosecha.objects.all()
    return render(request, 'formularios/datos.html', {'datosCosecha': datosCosecha} )

