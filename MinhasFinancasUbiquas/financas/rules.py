from django.core.urlresolvers import reverse
from .models import LancamentoFinanceiro

#Estudar sobre classes abstratas em python
#Estudar sobre validações no deleteview
#Estudar Exceptions no Django
#Estudar sobre Mixins
class Rules():
    def ValidateDelete(model):
        pass
    
    def ValidateSave(model):
        pass

class SaqueRules(Rules):
    def ValidateDelete(self, model):
        lanctosPagos = LancamentoFinanceiro.Objects.filter(status = STATUS_CHOICES.Pago)
        if not lanctosPagos is None:
            return django.http.HttpResponseBadRequest("Saque não pode ser apagado pois possui lançamentos financeiros pagos.") 

    def ValidateSave(self, model):
        # Se valor do saque for diferente do valor total de lançamentos vinculados ao saque, subir exceção 
        # totalLanctos = LancamentoFinanceiro.Objects.Agre  
        pass