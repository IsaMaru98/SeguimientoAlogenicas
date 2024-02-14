from django.contrib import admin

from . import models
from import_export.admin import ImportExportModelAdmin
# class CosechaAdmin(admin.ModelAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         if obj is None:
#             # Si el objeto es nuevo, usa un formulario sin la clave primaria
#             self.exclude = ( 'densidadCosecha', 'totalObtenidas', 'cosechaId')
#         else:
#             # Si el objeto ya existe, usa el formulario por defecto
#             self.exclude = ()
#         return super(CosechaAdmin, self).get_form(request, obj, **kwargs)
## Este objeto hace que en la consola de administrador no me pida una clave primaria ya que la estoy autogenerando con la función definida en models.py
class CosechaAdmin(admin.ModelAdmin):
    exclude = ('densidadCosecha', 'totalObtenidas', 'cosechaId')
    list_display = ('cci', 'loteCosecha', 'fechaCosecha', 'totalObtenidas', 'cosechaId')
    list_filter = ('cci', 'loteCosecha')

class CrioAdmin(admin.ModelAdmin):
    exclude = ('totalCrio', 'crioId')
    list_display = ('cci', 'crioId', 'fechaCrio', 'totalCrio', 'cosecha')
    list_filter = ('cci',)

class SiembraAdmin(admin.ModelAdmin):
    exclude = ('densidadSiembra','siembraId', 'totalSiembra')
    list_display = ('cci', 'loteSimbra', 'fechaSiembra', 'medioSiembra','siembraId')
    list_filter = ('areaFrascosSiembra', 'loteSimbra', 'medioSiembra')  # Add any filters you want
    search_fields = ('siembraId', 'loteSimbra')  # Add any fields you want to search by


class DatoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
    exclude = ( 'generaciones', 'tiempoDuplicacion', 'relacionExpansion', 'loteDatos', 'pase', 'densidadCosecha', 'densidadSiembra', 'datoId')
    list_display = ('cci', 'loteDatos','medioSiembra', 'datoId')
    list_filter = ('loteDatos',)  # Add any filters you want
    search_fields = ('loteDatos',)
admin.site.register(models.Cosecha, CosechaAdmin)
admin.site.register(models.Siembra, SiembraAdmin)
admin.site.register(models.Crio, CrioAdmin)
admin.site.register(models.Dato, DatoAdmin)