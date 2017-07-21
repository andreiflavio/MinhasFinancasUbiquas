from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from .models import Classificacao

class ClassificacaoListView(ListView):
    model = Classificacao

    def get_queryset(self, **kwargs):
        return Classificacao.objects.all()

class ClassificacaoCreate(CreateView):
    model = Classificacao
    template_name = 'core/form_crud.html'
    fields = ['nome']

class ClassificacaoUpdate(UpdateView):
    model = Classificacao
    template_name = 'core/form_crud.html'
    fields = ['nome']

class ClassificacaoDelete(DeleteView):
    model = Classificacao
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('financas:classificacao_list')