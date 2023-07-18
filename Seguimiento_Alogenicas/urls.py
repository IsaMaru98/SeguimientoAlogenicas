
from django.contrib import admin
from django.urls import path, include 
<<<<<<< HEAD
from formularios.api import api 

=======
from .api import api , router
>>>>>>> master

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('formularios.urls')),
<<<<<<< HEAD
    path('api/', api.urls), 

=======
    path("api/", api.urls),
>>>>>>> master
]
