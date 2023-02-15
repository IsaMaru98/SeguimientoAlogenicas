from django.shortcuts import render, HttpResponse

from .models import Cosecha

from django.http import HttpResponseRedirect

from .forms import CosechaForm 
# Create your views here.

## en esta función llamo los datos de Cosecha con el objects.all() y estos los paso por medio de un diccionario al html 
# en el archivo html puedo mostrar estos datos del objeto usando un ciclo for 

def home(request): 
    datosCosecha = Cosecha.objects.all()
    return render(request, 'formularios/home.html', {'datosCosecha': datosCosecha} )

def datos(request): 
    return render(request, 'formularios/datos.html', {} )

def get_datos(request): 

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CosechaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/datos/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CosechaForm()

    return render(request, 'formularios/home.html', {'form': form})