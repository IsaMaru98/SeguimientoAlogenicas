from django import forms
from . import models

class CosechaForm(forms.Form):
    loteCosecha = forms.CharField(label='Lote:', max_length=100)
    fechaCosecha = forms.DateField(label='Fecha:')
    paseCosecha = forms.CharField(max_length=50 ,label='Pase:')
    areaFrascosCosecha = forms.ChoiceField(choices=[("",""),(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'), (0, 'Crioviales')] ,label='Tipo de frasco:')
    numFrascosCosecha = forms.IntegerField(label='Número de frascos:') 
    numCelulasObtenidas = forms.FloatField(label='Numero de células obtenidas:')
    viabilidadCosecha = forms.IntegerField(label='Viabilidad: ')
    
class SiembraForm(forms.Form): 
    loteSimbra = forms.CharField(max_length=50, label='Lote Siembra:') 
    fechaSiembra = forms.DateField(label='Fecha Siembra:')
    paseSiembra = forms.CharField(max_length=50, label='Pase Siembra:')
    areaFrascosSiembra = forms.ChoiceField(choices=[("",""),(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'), (0, 'Crioviales')], label='Tipo de frasco Siembra:')
    numFrascosSiembra = forms.IntegerField(label='Número de frascos d Siembra:')
    numCelulasSembradasXFrasco = forms.FloatField(label='Número de células sembradas por frasco: ')

class CrioForm(forms.ModelForm): 

    class Meta: 
        model =  models.Crio
        fields = ['numCelulasXVial' ,  'numViales'] 
        labels = {'numCelulasXVial' : 'Número de células por vial:' , 'numViales': 'Número de viales'}