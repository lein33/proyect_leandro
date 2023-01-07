from django.contrib import admin
from apps.persona.models import Persona
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class DataCategoria(resources.ModelResource):
    class Meta:
        model = Persona
        import_id_fields = ('dni',)

class DataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['dni']
    list_display = ('dni','nombre', 'edad', 'sexo', 'correo', 'pais', 'provincia', 'direccion', 'cod_postal', 'celular')
    resource_class = DataCategoria

admin.site.register(Persona,DataAdmin)
