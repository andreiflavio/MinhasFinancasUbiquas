from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from . models import Pessoa
from MinhasFinancasUbiquas.financas.models import LancamentoFinanceiro

# Create your views here.

def index(request):
    ##Esta view para utilizar django forms
    
    ##Trazer listas filtradas por data
    lancamentos = LancamentoFinanceiro.objects.all()    
    ##Monta objeto com Total de contas a pagar não pagas
    totalContasAPagar = lancamentos.count()    
    ##Montar objeto com Saldo de gastos gerais para usar (saldo da conta carteira)
    totalSaldoGastosGerais = lancamentos.count()
    ##Montar objeto com Saldo conta bancária
    saldoEmConta = lancamentos.count()
    ##Montar objeto Saldo da fatura atual do cartão de crédito principal
    saldoFaturaCartaoCredito = lancamentos.count()
    
    context = {
        'totalContasAPagar': totalContasAPagar,
        'totalSaldoGastosGerais': totalSaldoGastosGerais,
        'saldoEmConta': saldoEmConta,
        'saldoFaturaCartaoCredito':saldoFaturaCartaoCredito,
    }    
    return render(request, 'core/index.html', context)

class CoreListView(ListView):
    pass

class CoreCreateView(CreateView):
    template_name = 'core/form_crud.html'

class CoreUpdateView(UpdateView):
    template_name = 'core/form_crud.html'

class CoreDeleteView(DeleteView):
    template_name = 'core/confirm_delete.html'    