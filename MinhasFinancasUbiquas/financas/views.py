from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from .models import Classificacao, Conta, CartaoCredito

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

class ContaListView(ListView):
    model = Conta

    def get_queryset(self, **kwargs):
        return Conta.objects.all()

class ContaCreate(CreateView):
    model = Conta
    template_name = 'core/form_crud.html'
    fields = ['nome', 'ehContaBancaria']

class ContaUpdate(UpdateView):
    model = Conta
    template_name = 'core/form_crud.html'
    fields = ['nome', 'ehContaBancaria']

class ContaDelete(DeleteView):
    model = Conta
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('financas:conta_list')

class CartaoCreditoListView(ListView):
    model = CartaoCredito

    def get_queryset(self, **kwargs):
        return CartaoCredito.objects.all()

class CartaoCreditoCreate(CreateView):
    model = CartaoCredito
    template_name = 'core/form_crud.html'
    fields = ['nome', 'numero', 'observacao']

class CartaoCreditoUpdate(UpdateView):
    model = CartaoCredito
    template_name = 'core/form_crud.html'
    fields = ['nome', 'numero', 'observacao']

class CartaoCreditoDelete(DeleteView):
    model = CartaoCredito
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('financas:cartaocredito_list')