from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string

from django.urls import reverse
from django.http import HttpResponseRedirect
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 

import math as ma 
# Create your views here.

## en esta función llamo los datos de Cosecha con el objects.all() y estos los paso por medio de un diccionario al html 
# en el archivo html puedo mostrar estos datos del objeto usando un ciclo for 
def home(request):
    return render(request, 'formularios/home.html', {})
@login_required
def cosecha(request): 

    if request.method == 'POST': 
        formCosecha = forms.CosechaForm(request.POST)
        formCosechaClean = forms.CosechaForm()
        if formCosecha.is_valid():
            if request.POST.get('action') == 'Guardar': 
                formCosecha.save() 
                return render(request, 'formularios/cosecha.html', {'formCosecha': formCosecha, 'success': True})
            elif request.POST.get('action') == 'Adicionar otro':
                return  render(request, 'formularios/cosecha.html', {'formCosecha':formCosechaClean} )
            else: 
                return  HttpResponseRedirect(reverse('datos'))

    # if a GET (or any other method) we'll create a blank form
    else:
        formCosecha = forms.CosechaForm()
    
    return render(request, 'formularios/cosecha.html', {'formCosecha': formCosecha} )

# def siembra(request): 
#     if request.method == 'POST': 
#         formSiembra = forms.SiembraForm(request.POST)
#         formSiembraClean = forms.SiembraForm()
#         if formSiembra.is_valid():
#             if request.POST.get('action') == 'Guardar': 
#                 formSiembra.save() 
#                 return render(request, 'formularios/siembra.html', {'formSiembra': formSiembra, 'success': True})
#             elif request.POST.get('action') == 'Adicionar otro':
#                 return  render(request, 'formularios/siembra.html', {'formSiembra':formSiembraClean} )
#             else: 
#                 return HttpResponseRedirect(reverse('datos'))
#     else:
#         formSiembra = forms.SiembraForm()
    
    # return render(request, 'formularios/siembra.html', {'formSiembra': formSiembra} )
@login_required
def siembra(request): 
    if request.method == 'POST': 
        formSiembra = forms.SiembraForm(request.POST)
        formSiembraClean = forms.SiembraForm()

        if formSiembra.is_valid():
            try:
                if request.POST.get('action') == 'Guardar': 
                    form_instance = formSiembra.save()
                    print("Form instance after saving:", form_instance)
                    return render(request, 'formularios/siembra.html', {'formSiembra': formSiembra, 'success': True})
                elif request.POST.get('action') == 'Adicionar otro':
                    return render(request, 'formularios/siembra.html', {'formSiembra': formSiembraClean})
                else: 
                    return HttpResponseRedirect(reverse('datos'))
            except Exception as e:
                print("Exception:", e)

    else:
        formSiembra = forms.SiembraForm()
    
    return render(request, 'formularios/siembra.html', {'formSiembra': formSiembra})
@login_required
def crio(request):

    if request.method == 'POST': 
        formCrio = forms.CrioForm(request.POST)
        formCrioClean = forms.CrioForm()
        if formCrio.is_valid():
            if request.POST.get('action') == 'Guardar': 
                formCrio.save() 
                return render(request, 'formularios/crio.html', {'formCrio': formCrio, 'success': True})
            elif request.POST.get('action') == 'Adicionar otro':
                return  render(request, 'formularios/crio.html', {'formCrio':formCrioClean} )
            else: 
                return  HttpResponseRedirect(reverse('datos'))
        
    else:
        formCrio = forms.CrioForm()
    
    return render(request, 'formularios/crio.html', {'formCrio': formCrio} )
@login_required
def datoForm(request):

    if request.method == 'POST': 
        formDato = forms.DatosForm(request.POST)
        if formDato.is_valid():
            if request.POST.get('action') == 'Guardar':
                formDato.save() 

                return render(request, 'formularios/formularioDatos.html', {'formDato': formDato, 'success': True})
            else: 
                return HttpResponseRedirect(reverse('datos'))
    
    else:
        formDato = forms.DatosForm()
    
    return render(request, 'formularios/formularioDatos.html', {'formDato': formDato} )
@login_required
def datos(request): 
    datos = models.Dato.objects.all()
    
    return render(request, 'formularios/datos.html', {'datos':datos} )
@login_required
def lotes(request): 
    datosCosecha = models.Cosecha.objects.all()
    datosSiembra = models.Siembra.objects.all()
    return render(request, 'formularios/lotes.html', {'datosCosecha':datosCosecha, 'datosSiembra':datosSiembra})

@login_required
def data_table(request): 

    data = models.Dato.objects.all()
    return render(request, 'data_table.html', {'data': data})
@login_required
def refresh_data(request):
    data = models.Dato.objects.all() 
    table_rows = render_to_string('table_rows.html', {'data': data})
    return HttpResponse(table_rows)

def salir(request):
    logout(request)
    return(redirect('/'))