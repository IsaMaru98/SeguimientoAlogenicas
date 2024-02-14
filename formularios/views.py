from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string

from django.urls import reverse
from django.http import HttpResponseRedirect
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Avg
import math as ma
# Create your views here.
from openpyxl import Workbook

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

    dSiembra = []
    rExpansion = []
    lotes = []
    promDensidadlot = []
    promDensidadPas = []
    promDensidadFras = []
    pase = []
    tipoFrasco = []
    
    queryset = models.Dato.objects.order_by('loteDatos')
    datos_cosechaProm = models.Cosecha.objects.values('loteCosecha').order_by('loteCosecha').annotate(promedio_densidad=Avg('densidadCosecha'))
    datos_cosechaPas = models.Cosecha.objects.values('paseCosecha').annotate(promedio_densidad=Avg('densidadCosecha'))
    datos_cosechaFras = models.Cosecha.objects.values('areaFrascosCosecha').annotate(promedio_densidad=Avg('densidadCosecha'))
    for dato in queryset:
        dSiembra.append(dato.densidadSiembra)
        rExpansion.append(dato.relacionExpansion)
    for item in datos_cosechaProm:
        lotes.append(item['loteCosecha'])
        promDensidadlot.append(item['promedio_densidad'])
    for item in datos_cosechaPas:
        pase.append(item['paseCosecha'])
        promDensidadPas.append(item['promedio_densidad'])
    for item in datos_cosechaFras:
        tipoFrasco.append(item['areaFrascosCosecha'])
        promDensidadFras.append(item['promedio_densidad'])

    return render (request, 'formularios/lotes.html', {'dSiembra':dSiembra,'rExpansion':rExpansion,'lotes':lotes,'promDensidadlot':promDensidadlot, 'pase':pase, 'tipoFrasco':tipoFrasco, 'promDensidadFras':promDensidadFras, 'promDensidadPas':promDensidadPas})

def dato_xlsx(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=datos.xlsx'

    # Crear libro de trabajo y hoja de cálculo
    wb = Workbook()
    ws = wb.active

    # Designar el modelo
    datos = models.Dato.objects.all()
    siembras = models.Siembra.objects.all()
    cosechas = models.Cosecha.objects.all()

    # Escribir encabezados
    headers = ['CCI', 'Id Siembra', 'Id Cosecha', 'Lote', 'Pase', 'Densidad de Cosecha', 'Densidad de Siembra',
               'Medio de Siembra', 'Generaciones', 'Tiempo de Duplicacion', 'Relacion Expansion']
    ws.append(headers)

    # Escribir datos
    for dato in datos:
        # Extract attributes from related models if needed
        id_siembra = str(dato.siembra)
        id_cosecha = str(dato.cosecha)

        row_data = [
            dato.cci, id_siembra, id_cosecha, dato.loteDatos, dato.pase, dato.densidadCosecha,
            dato.densidadSiembra, dato.medioSiembra, dato.generaciones, dato.tiempoDuplicacion, dato.relacionExpansion
        ]
        ws.append(row_data)

    # Guardar el libro de trabajo en el objeto response
    wb.save(response)

    return response


def salir(request):
    logout(request)
    return(redirect('/'))
