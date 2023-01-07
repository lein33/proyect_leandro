from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.vehiculo.forms import VehiculoForm
from apps.vehiculo.models import Vehiculo 
from django.views.generic import CreateView
from apps.persona.forms import PersonaFrom
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
def vehiculo_list(request):
    vehiculo = Vehiculo.objects.all()
    contexto ={'vehiculos': vehiculo}
    return render(request, 'vehiculo/tables_vehiculo.html', contexto)

def vehiculo_view(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculo:lista')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/crear_vehiculo.html', {'form': form})

def saludoV(request):
    return render(request, 'vehiculo/index.html')

class vehiculo_persona(CreateView):
    model = Vehiculo
    template_name = 'vehiculo/crear_vehiculo.html'
    form_class = VehiculoForm
    second_form_class = PersonaFrom
    success_url = reverse_lazy('vehiculo:lista_vehiculos')

    def get_context_data(self, **kwargs):
        context = super(vehiculo_persona, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            vehi_p = form.save(commit=False)
            vehi_p.persona = form2.save()
            vehi_p.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))