
from django.contrib import admin
from django.urls import path, include 
from formularios.api import api 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('formularios.urls')),
    path('api/', api.urls), 

]
