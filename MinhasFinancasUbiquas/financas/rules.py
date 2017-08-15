from django.db.models import Sum

# Regras de negócio cadastro de Saque
def beforeDeleteSaque(model, listaLanctosPagos):
    if (listaLanctosPagos.count() > 0):
        raise Exception("Saque não pode ser apagado pois possui lançamentos financeiros vinculados a ele.") 

def beforeSaveSaque(model, listaLanctosPagos):
    if listaLanctosPagos.count() > 0:
        valorTotalLanctos = listaLanctosPagos.aggregate(total_valor = Sum("valor"))        
        if float(model.valor_saque) != valorTotalLanctos['total_valor']:
            raise Exception("Valor dos lançamentos financeiros vinculados ao saque não conferem com valor do saque")