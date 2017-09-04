from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import LancamentoFinanceiro


class LancamentoFinanceiroForm(forms.ModelForm):

    class Meta:
        model = LancamentoFinanceiro
        fields = ('descricao', 'data', 'tipo', 'valor', 'status',  'classificacao', 'conta',)

    def __init__(self, *args, **kwargs):
        super(LancamentoFinanceiroForm, self).__init__(*args, **kwargs)
        self.fields['descricao'].required = True
        self.fields['descricao'].label = 'Descrição'
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})