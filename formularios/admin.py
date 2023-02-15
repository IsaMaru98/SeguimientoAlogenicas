from django.contrib import admin

from . import models 


# Register your models here.

## Este objeto hace que en la consola de administrador no me pida una clave primaria ya que la estoy autogenerando con la función definida en models.py
class CosechaAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            # Si el objeto es nuevo, usa un formulario sin la clave primaria
            self.exclude = ('idCosecha',)
        else:
            # Si el objeto ya existe, usa el formulario por defecto
            self.exclude = ()
        return super(CosechaAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(models.Cosecha, CosechaAdmin)
admin.site.register(models.Siembra)
admin.site.register(models.Crio)