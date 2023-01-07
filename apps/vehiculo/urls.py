from django.urls import path
from apps.vehiculo.views import vehiculo_view,vehiculo_list,saludoV, vehiculo_persona
app_name = 'vehiculo'
urlpatterns = [
    path('', saludoV, name='index'),
    path('newv/', vehiculo_view, name='crear_vehiculo'),
    path('listv/', vehiculo_list, name='listar_vehiculo'),
    path('listv_p/', vehiculo_persona.as_view(), name='lista_vehiculos'),

]



