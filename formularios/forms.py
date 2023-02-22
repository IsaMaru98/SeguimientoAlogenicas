from django import forms
from . import models

class CosechaForm(forms.ModelForm):
    class Meta: 
        model = models.Cosecha
        fields = ['cci', 'loteCosecha','fechaCosecha','paseCosecha','areaFrascosCosecha','numFrascosCosecha','numCelulasObtenidas','viabilidadCosecha', 'confluenciaCosecha',
    'tiempoCultivoDias', 'siembra']
        labels = {'loteCosecha': 'Lote:','fechaCosecha': 'Fecha cosecha:','paseCosecha': 'Pase cosecha:','areaFrascosCosecha':'Tipo de frasco Cosecha:','numFrascosCosecha': 'Número de frascos de cosecha:', 'numCelulasObtenidas': 'Número total de células obtenidas (x10e6):','viabilidadCosecha': 'Viabilidad obtenida:', 'cci': 'CCI:', 'confluenciaCosecha': 'Confluencia (%):',
    'tiempoCultivoDias': 'Tiempo de cultivo (días):', 'siembra': 'Siembra'}
        widgets = {
            'fechaCosecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
class SiembraForm(forms.ModelForm):
    class Meta: 
        model = models.Siembra  
        fields = ['cci','loteSimbra','fechaSiembra','paseSiembra','areaFrascosSiembra', 'numFrascosSiembra','numCelulasSembradasXFrasco']
        labels = {'loteSimbra': 'Lote:' ,'fechaSiembra': 'Fecha Siembra:','paseSiembra':'Pase Siembra:','areaFrascosSiembra': 'Tipo de frasco Siembra:' , 'numFrascosSiembra': 'Número de frascos de Siembra:' ,'numCelulasSembradasXFrasco': 'Número de células sembradas por frasco (x10e6):', 'cci': 'CCI:' }
        widgets = {
            'fechaSiembra': forms.DateInput(attrs={'type': 'date'}),
        }

class CrioForm(forms.ModelForm): 

    class Meta: 
        model =  models.Crio
        fields = ['cci', 'numCelulasXVial' ,  'numViales'] 
        labels = {'numCelulasXVial' : 'Número de células por vial:' , 'numViales': 'Número de viales',  'cci': 'CCI:'}