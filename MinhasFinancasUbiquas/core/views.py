from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from . models import Pessoa

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

class PessoaListView(ListView):

    model = Pessoa

    def get_queryset(self, **kwargs):
        return Pessoa.objects.all()

class PessoaCreate(CreateView):
    model = Pessoa
    template_name = 'core/form_crud.html'
    fields = ['nome']

class PessoaUpdate(UpdateView):
    model = Pessoa
    template_name = 'core/form_crud.html'
    fields = ['nome']
    

class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('core:pessoa_list')
    
