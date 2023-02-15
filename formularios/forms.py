from django import forms

class CosechaForm(forms.Form):
    loteCosecha = forms.CharField(label='Lote cosecha: ', max_length=100)