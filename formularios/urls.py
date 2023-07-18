from django.urls import path 
from . import views 
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

urlpatterns = [
    path('', views.home, name='home'),
    path('datos/', views.datos, name='datos'),
    path('cosecha/', views.cosecha, name='formularioCosecha'),
    path('siembra/', views.siembra, name='formularioSiembra'), 
    path('crio/',views.crio, name='formularioCrio'),
    path('formulario_datos/',views.datoForm, name="formularioDato"), 
    path('lotes/', views.lotes, name='lotes'),
    path("api/", api.urls),
]