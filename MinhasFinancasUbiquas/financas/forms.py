from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import LancamentoFinanceiro, Classificacao, Conta, CartaoCredito


class FinancasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FinancasForm, self).__init__(*args, **kwargs)
        for fieldName in self.fields:            
            self.fields[fieldName].required = True          
            self.fields[fieldName].widget.attrs.update({'class': 'form-control'})
    
class LancamentoFinanceiroForm(FinancasForm):

    class Meta:
        model = LancamentoFinanceiro
        fields = ('descricao', 'data', 'tipo', 'valor', 'status',  'classificacao', 'conta',)


class ClassificacaoForm(FinancasForm):

    class Meta:
        model = Classificacao
        fields = ('nome', )    

class ContaForm(FinancasForm):

    class Meta:
        model = Conta
        fields = ('nome', 'ehContaBancaria', )

class CartaoCreditoForm(FinancasForm):

    class Meta:
        model = CartaoCredito
        fields = ('nome', 'bandeira','valor_limite', 'dia_fechamento_fatura', 'dia_vencimento_fatura', 'conta', )