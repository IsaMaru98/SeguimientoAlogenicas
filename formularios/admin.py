from django.contrib import admin

from . import models 


# Register your models here.

## Este objeto hace que en la consola de administrador no me pida una clave primaria ya que la estoy autogenerando con la función definida en models.py
class CosechaAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            # Si el objeto es nuevo, usa un formulario sin la clave primaria
            self.exclude = ( 'densidadCosecha', 'totalObtenidas', 'cosechaId')
        else:
            # Si el objeto ya existe, usa el formulario por defecto
            self.exclude = ()
        return super(CosechaAdmin, self).get_form(request, obj, **kwargs)

class CrioAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            # Si el objeto es nuevo, usa un formulario sin la clave primaria
            self.exclude = ('totalCrio',)
        else:
            # Si el objeto ya existe, usa el formulario por defecto
            self.exclude = ()
        return super(CrioAdmin, self).get_form(request, obj, **kwargs)

class SiembraAdmin(admin.ModelAdmin):
    list_display = ('cci', 'medioSiembra', 'loteSimbra', 'fechaSiembra', 'paseSiembra', 'areaFrascosSiembra', 'numFrascosSiembra', 'numCelulasSembradasXFrasco', 'densidadSiembra', 'siembraId', 'totalSiembra')
    list_filter = ('paseSiembra', 'areaFrascosSiembra', 'fechaSiembra', 'loteSimbra')  # Add any filters you want
    search_fields = ('siembraId', 'loteSimbra')  # Add any fields you want to search by

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            # Si el objeto es nuevo, usa un formulario sin la clave primaria
            self.exclude = ('densidadSiembra','siembraId', 'totalSiembra')
        else:
            # Si el objeto ya existe, usa el formulario por defecto
            self.exclude = ()
        return super(SiembraAdmin, self).get_form(request, obj, **kwargs)

class DatoAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            # Si el objeto es nuevo, usa un formulario sin la clave primaria
            self.exclude = ( 'generaciones', 'tiempoDuplicacion', 'relacionExpansion')
        else:
            # Si el objeto ya existe, usa el formulario por defecto
            self.exclude = ()
        return super(DatoAdmin, self).get_form(request, obj, **kwargs)
admin.site.register(models.Cosecha, CosechaAdmin)
admin.site.register(models.Siembra, SiembraAdmin)
admin.site.register(models.Crio, CrioAdmin)
admin.site.register(models.Dato, DatoAdmin)