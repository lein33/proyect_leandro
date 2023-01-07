from django.urls import path
from apps.pbv.views import pvb_list, pbv_delete, crear_listar

app_name = 'pbv'
urlpatterns = [
    path('pbv_list/', pvb_list, name='listar'),
    path('pbv_del/<int:idpbv>', pbv_delete, name='eliminar'),
    path('pbv2/', crear_listar.as_view(), name='lista'),

]