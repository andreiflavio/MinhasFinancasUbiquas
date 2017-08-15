# Regras de negócio cadastro de Saque
def beforeDeleteSaque(model, listaLanctosPagos):
    if (listaLanctosPagos.count() > 0):
        raise Exception("Saque não pode ser apagado pois possui lançamentos financeiros vinculados a ele.") 

def doBeforeSave(sender, **kwargs):
    # Se valor do saque for diferente do valor total de lançamentos vinculados ao saque, subir exceção 
    # totalLanctos = LancamentoFinanceiro.Objects.Agre  
    pass

