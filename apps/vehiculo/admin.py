from django.contrib import admin

from apps.vehiculo.models import Vehiculo, Mantenimiento

admin.site.register(Vehiculo)
admin.site.register(Mantenimiento)
