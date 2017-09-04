from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from . models import Pessoa

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

class CoreListView(ListView):
    pass

class CoreCreateView(CreateView):
    template_name = 'core/form_crud.html'

class CoreUpdateView(UpdateView):
    template_name = 'core/form_crud.html'

class CoreDeleteView(DeleteView):
    template_name = 'core/confirm_delete.html'    