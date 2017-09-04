from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.forms import modelformset_factory, inlineformset_factory
from django.http.response import HttpResponseRedirect
from .models import Classificacao, Conta, CartaoCredito, LancamentoFinanceiro
from MinhasFinancasUbiquas.core.views import CoreCreateView, CoreUpdateView, CoreDeleteView, CoreListView

class ClassificacaoListView(CoreListView):
    model = Classificacao

class ClassificacaoCreate(CoreCreateView):
    model = Classificacao    
    fields = ['nome']

class ClassificacaoUpdate(CoreUpdateView):
    model = Classificacao    
    fields = ['nome']

class ClassificacaoDelete(CoreDeleteView):
    model = Classificacao    
    success_url = reverse_lazy('financas:classificacao_list')

class ContaListView(CoreListView):
    model = Conta

class ContaCreate(CoreCreateView):
    model = Conta    
    fields = ['nome', 'ehContaBancaria']

class ContaUpdate(CoreUpdateView):
    model = Conta    
    fields = ['nome', 'ehContaBancaria']

class ContaDelete(CoreDeleteView):
    model = Conta    
    success_url = reverse_lazy('financas:conta_list')

class CartaoCreditoListView(CoreListView):
    model = CartaoCredito

class CartaoCreditoCreate(CoreCreateView):
    model = CartaoCredito    
    fields = ['nome', 'numero', 'dia_fechamento_fatura','observacao']

class CartaoCreditoUpdate(CoreUpdateView):
    model = CartaoCredito    
    fields = ['nome', 'numero', 'dia_fechamento_fatura','observacao']

class CartaoCreditoDelete(CoreDeleteView):
    model = CartaoCredito
    success_url = reverse_lazy('financas:cartaocredito_list')

class LancamentoFinanceiroListView(ListView):
    model = LancamentoFinanceiro

    def get_queryset(self, **kwargs):           
        var_get_search = self.request.GET.get('search_box')
        return LancamentoFinanceiro.getLanctos(var_get_search)

class LancamentoFinanceiroCreate(CoreCreateView):
    model = LancamentoFinanceiro
    fields = ['descricao', 'data', 'tipo', 'valor', 'status', 'classificacao', 'conta']

class LancamentoFinanceiroUpdate(CoreUpdateView):
    model = LancamentoFinanceiro
    fields = ['descricao', 'data', 'tipo', 'valor', 'status',  'classificacao', 'conta']

class LancamentoFinanceiroDelete(CoreDeleteView):    
    model = LancamentoFinanceiro
    success_url = reverse_lazy('financas:lancamentofinanceiro_list')
