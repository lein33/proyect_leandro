from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.persona.forms import PersonaFrom
from apps.persona.models import Persona
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
def saludoP(request):
    return render(request, 'persona/index.html')

def persona_view(request):
    if request.method == 'POST':
        form = PersonaFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('persona:index')
    else:
        form = PersonaFrom()
    return render(request, 'persona/indexp.html', {'form': form})

def persona_list(request):
    persona = Persona.objects.all().order_by('dni')
    contexto ={'personas': persona}
    return render(request, 'persona/tables_persona.html', contexto)

def persona_edit(request, dni):
    persona = Persona.objects.get(dni=dni)
    if request.method == 'GET':
        form = PersonaFrom(instance=persona)
    else:
        form = PersonaFrom(request.POST, instance=persona)
        if form.is_valid():
            form.save()
        return redirect('persona:persona_listar')
    return render(request,'persona/indexp.html',{'form':form})
def persona_del(request,dni):
    persona = Persona.objects.get(dni=dni)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona:persona_listar')
    return render(request,'persona/persona_del.html',{'persona':persona})

class PersonaList(ListView):
    model = Persona
    template_name = 'persona/tables_persona.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaFrom
    template_name = 'persona/indexp.html'    
    success_url = reverse_lazy('persona:persona_listar')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaFrom
    template_name = 'persona/indexp.html'    
    success_url = reverse_lazy('persona:persona_listar')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'persona/persona_del.html'    
    success_url = reverse_lazy('persona:persona_listar')
