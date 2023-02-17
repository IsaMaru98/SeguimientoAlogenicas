from django import forms
from . import models

class CosechaForm(forms.ModelForm):
    class Meta: 
        model = models.Cosecha
        fields = ['loteCosecha','fechaCosecha','paseCosecha','areaFrascosCosecha','numFrascosCosecha','numCelulasObtenidas','viabilidadCosecha']
        labels = {'loteCosecha': 'Lote: ','fechaCosecha': 'Fecha cosecha: ','paseCosecha': 'Pase cosecha: ','areaFrascosCosecha': 'Tipo de frasco Cosecha: ','numFrascosCosecha': 'Número de frascos de cosecha: ', 'numCelulasObtenidas': 'Número de células obtenidas: ','viabilidadCosecha': 'Viabilidad obtenida: '}
    
class SiembraForm(forms.ModelForm):
    class Meta: 
        model = models.Siembra  
        fields = ['loteSimbra','fechaSiembra','paseSiembra','areaFrascosSiembra', 'numFrascosSiembra','numCelulasSembradasXFrasco']
        labels = {'loteSimbra': 'Lote: ' ,'fechaSiembra': 'Fecha Siembra:','paseSiembra':'Pase Siembra:','areaFrascosSiembra': 'Tipo de frasco Siembra:' , 'numFrascosSiembra': 'Número de frascos de Siembra:' ,'numCelulasSembradasXFrasco': 'Número de células sembradas por frasco: ' }

class CrioForm(forms.ModelForm): 

    class Meta: 
        model =  models.Crio
        fields = ['numCelulasXVial' ,  'numViales'] 
        labels = {'numCelulasXVial' : 'Número de células por vial:' , 'numViales': 'Número de viales'}