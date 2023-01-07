from django.urls import path
from apps.persona.views import saludoP,persona_view, persona_list, persona_edit,persona_del
from apps.persona.views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete
app_name = 'persona'
urlpatterns = [
    path('saludop/', saludoP, name='index'),
   # path('newp/', persona_view, name='crear_persona'),
    path('newp/', PersonaCreate.as_view(), name='crear_persona'),

    path('listp/', PersonaList.as_view(), name='persona_listar'),
 #   path('editp/<str:dni>/', persona_edit, name='persona_editar'),
    path('editp/<str:pk>/', PersonaUpdate.as_view(), name='persona_editar'),
    path('delp/<str:pk>/', PersonaDelete.as_view(), name='persona_eliminar'),
    
#    path('delp/<str:dni>/', persona_del, name='persona_eliminar'),


]
