
from django.contrib import admin
from django.urls import path, include 
from .api import api , router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('formularios.urls')),
    path("api/", api.urls),
]
