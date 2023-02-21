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
            celulasObtenidas = formCosecha.cleaned_data['numCelulasObtenidas']
            numFrascosCosecha = formCosecha.cleaned_data['numFrascosCosecha']
            areaFrascosCosecha = formCosecha.cleaned_data['areaFrascosCosecha']
            

            r = ((celulasObtenidas*1000000)/(areaFrascosCosecha*numFrascosCosecha))

            densidadCosecha = round(r, 2 )
    

            formCosecha.save()
            # redirect to a new URL:
            return render(request, 'formularios/datos.html', {'densidadCosecha': densidadCosecha})

    # if a GET (or any other method) we'll create a blank form
    else:
        formCosecha = forms.CosechaForm()
    
    return render(request, 'formularios/formularioCosecha.html', {'formCosecha': formCosecha} )

def siembraForm(request): 
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        formSiembra= forms.SiembraForm(request.POST)
        
        if formSiembra.is_valid():
            celulasSembradas = formSiembra.cleaned_data['numCelulasSembradasXFrasco']
            areaFrascoSiembra = formSiembra.cleaned_data['areaFrascosSiembra']

            densidadSiembra = round((celulasSembradas*1000000)/ areaFrascoSiembra, 2)
            formSiembra.save()
            # redirect to a new URL:
    
            return render(request, 'formularios/datos.html', {'densidadSiembra': densidadSiembra})
    else:
        formSiembra = forms.SiembraForm()
    
    return render(request, 'formularios/formularioSiembra.html', {'formSiembra': formSiembra} )

def crioForm(request):

    def totalCrio(a,b):
        result = a*b 

        return result 


    if request.method == 'POST': 
        formCrio = forms.CrioForm(request.POST)
        if formCrio.is_valid():
            numCelulasXVial = formCrio.cleaned_data['numCelulasXVial']
            numViales = formCrio.cleaned_data['numViales']

            total = totalCrio(numCelulasXVial,numViales)
            formCrio.save() 

            return render(request, 'formularios/datos.html', {'total':total})
    
    else:
        formCrio = forms.CrioForm()
    
    return render(request, 'formularios/formularioCrio.html', {'formCrio': formCrio} )

def datos(request): 
    datosCosecha = models.Cosecha.objects.all()
    return render(request, 'formularios/datos.html', {'datosCosecha': datosCosecha} )

