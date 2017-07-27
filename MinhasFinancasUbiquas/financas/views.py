from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.forms import modelformset_factory, inlineformset_factory
from django.http.response import HttpResponseRedirect
from .models import Classificacao, Conta, CartaoCredito, Saque, LancamentoFinanceiro
from .forms import SaqueForm

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

class SaqueListView(ListView):
    model = Saque

    def get_queryset(self, **kwargs):
        return Saque.objects.all()
"""
class SaqueCreate(CreateView):
    model = Saque
    template_name = 'financas/form_saque_create.html',    
    fields = ['descricao', 'conta', 'data_saque']

class SaqueUpdate(UpdateView, pk):
    model = Saque
    template_name = 'financas/form_saque_create.html',
    fields = ['descricao', 'conta', 'data_saque']
"""
class SaqueDelete(DeleteView):
    model = Saque
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('financas:saque_list')

def SaqueCreate(request):
    if request.method == 'POST':
        form = SaqueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('financas:saque_list')
    else:
        form = SaqueForm()
    return render(request, 'financas/form_saque_create.html', {'form': form})

def SaqueUpdate(request, pk):
    saque = get_object_or_404(Saque, pk=pk)
    context = {}
    if request.method == 'POST':
        form = SaqueForm(request.POST, request.FILES, instance=saque)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(saque.get_absolute_url())
    else:
        form = SaqueForm(instance=saque)
    context['listaLanctos'] = LancamentoFinanceiro.objects.filter(saque = pk)
    context['form'] = form
    return render(request, 'financas/form_saque_create.html', context)