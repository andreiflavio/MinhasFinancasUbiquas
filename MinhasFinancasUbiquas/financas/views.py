from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.forms import modelformset_factory, inlineformset_factory
from django.http.response import HttpResponseRedirect
from .models import Classificacao, Conta, CartaoCredito, LancamentoFinanceiro

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
    fields = ['nome', 'numero', 'dia_fechamento_fatura','observacao']

class CartaoCreditoUpdate(UpdateView):
    model = CartaoCredito
    template_name = 'core/form_crud.html'
    fields = ['nome', 'numero', 'dia_fechamento_fatura','observacao']

class CartaoCreditoDelete(DeleteView):
    model = CartaoCredito
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('financas:cartaocredito_list')

class LancamentoFinanceiroListView(ListView):
    model = LancamentoFinanceiro

    def get_queryset(self, **kwargs):           
        var_get_search = self.request.GET.get('search_box')
        return LancamentoFinanceiro.getLanctos(var_get_search)

class LancamentoFinanceiroCreate(CreateView):
    model = LancamentoFinanceiro
    template_name = 'core/form_crud.html'
    fields = ['descricao', 'data', 'tipo', 'valor', 'status', 'classificacao', 'conta']

class LancamentoFinanceiroUpdate(UpdateView):
    model = LancamentoFinanceiro
    template_name = 'core/form_crud.html'
    fields = ['descricao', 'data', 'tipo', 'valor', 'status',  'classificacao', 'conta']

class LancamentoFinanceiroDelete(DeleteView):
    model = LancamentoFinanceiro
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('financas:lancamentofinanceiro_list')
