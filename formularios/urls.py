from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('datos/', views.datos, name='datos'),
    path('cosecha/', views.cosecha, name='formularioCosecha'),
    path('siembra/', views.siembra, name='formularioSiembra'),
    path('crio/',views.crio, name='formularioCrio'),
    path('formulario_datos/',views.datoForm, name="formularioDato"),
    path('lotes/', views.lotes, name='lotes'),
    path('salir/',views.salir, name='salir'),
    path('dato_xlsx/',views.dato_xlsx, name='dato_xlsx'),

]
