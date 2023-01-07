from django.shortcuts import render,redirect
from apps.pbv.models import pbv
from apps.pbv.forms import prueba

from django.views.generic import CreateView
from django.urls import reverse_lazy

def pvb_list(request):
    pbv_list = pbv.objects.all()
    context = {'pbv': pbv_list,'title':'tabla'}
    return render(request,'boostrap/index.html',context)


class crear_listar(CreateView):
    model = pbv
    template_name = 'boostrap/index.html'
    form_class = prueba
    success_url = reverse_lazy('pbv:lista')

    def get_context_data(self, **kwargs):
        context = super(crear_listar, self).get_context_data(**kwargs)
        #context['form'] = self.form_class(self.request.GET)
        context['form'] = self.form_class()
        context['pbv'] =  pbv.objects.all()
        return context

def pbv_delete(request, idpbv):
    obj_pbv = pbv.objects.get(idpbv=idpbv)
    if request.method =='POST':
        obj_pbv.delete()
        return redirect('pbv:lista')
    return render(request,'boostrap/conf_delet.html')