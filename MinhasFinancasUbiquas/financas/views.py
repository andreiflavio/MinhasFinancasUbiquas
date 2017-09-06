from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.forms import modelformset_factory, inlineformset_factory
from django.http.response import HttpResponseRedirect
from .models import Classificacao, Conta, CartaoCredito, LancamentoFinanceiro
from MinhasFinancasUbiquas.core.views import CoreCreateView, CoreUpdateView, CoreDeleteView, CoreListView
from .forms import LancamentoFinanceiroForm, ClassificacaoForm, ContaForm, CartaoCreditoForm

class ClassificacaoListView(CoreListView):
    model = Classificacao

class ClassificacaoCreate(CoreCreateView):
    model = Classificacao    
    form_class = ClassificacaoForm

class ClassificacaoUpdate(CoreUpdateView):
    model = Classificacao    
    form_class = ClassificacaoForm

class ClassificacaoDelete(CoreDeleteView):
    model = Classificacao    
    success_url = reverse_lazy('financas:classificacao_list')

class ContaListView(CoreListView):
    model = Conta

class ContaCreate(CoreCreateView):
    model = Conta    
    form_class = ContaForm

class ContaUpdate(CoreUpdateView):
    model = Conta    
    form_class = ContaForm

class ContaDelete(CoreDeleteView):
    model = Conta    
    success_url = reverse_lazy('financas:conta_list')

class CartaoCreditoListView(CoreListView):
    model = CartaoCredito

class CartaoCreditoCreate(CoreCreateView):
    model = CartaoCredito    
    form_class = CartaoCreditoForm

class CartaoCreditoUpdate(CoreUpdateView):
    model = CartaoCredito    
    form_class = CartaoCreditoForm

class CartaoCreditoDelete(CoreDeleteView):
    model = CartaoCredito
    success_url = reverse_lazy('financas:cartaocredito_list')

class LancamentoFinanceiroListView(CoreListView):
    model = LancamentoFinanceiro

    def get_queryset(self, **kwargs):           
        var_get_search = self.request.GET.get('search_box')
        return LancamentoFinanceiro.getLanctos(var_get_search)

class LancamentoFinanceiroCreate(CoreCreateView):
    model = LancamentoFinanceiro
    form_class = LancamentoFinanceiroForm

class LancamentoFinanceiroUpdate(CoreUpdateView):
    model = LancamentoFinanceiro
    form_class = LancamentoFinanceiroForm

class LancamentoFinanceiroDelete(CoreDeleteView):    
    model = LancamentoFinanceiro
    success_url = reverse_lazy('financas:lancamentofinanceiro_list')
