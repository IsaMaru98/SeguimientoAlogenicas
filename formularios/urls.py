from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('datos/', views.datos, name='datos'),
    path('formulario_cosecha/', views.cosechaForm, name='formularioCosecha'),
    path('formulario_siembra/', views.siembraForm, name='formularioSiembra'), 
    path('formulario_criopreservacion/',views.crioForm, name='formularioCrio')
]