from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from MinhasFinancasUbiquas.core.models import Pessoa

# Documentação base para implementação deste model: https://docs.djangoproject.com/en/1.11/topics/db/models/
class Classificacao(models.Model):
    """
    Neste cadastro serão definidos como usuário deseja classificar seus lançamentos financeiros. Exemplo: 
    Gastos Férias, Namoro, Passeios, Gastos Essenciais, Gastos Supérfluos, entre outras categorias que o usuário deseja.
    """
    nome = models.CharField("Nome", max_length = 80)

    def get_absolute_url(self):
        return reverse('financas:classificacao_list')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Classificação'
        verbose_name_plural = 'Classificações'
        ordering = ["pk"]

class Conta(models.Model):
    """
    Neste cadastro usuário vai cadastrar suas contas bancárias/não bancárias. Exemplo: Conta Carteira 
    (para indicar dinheiro que ele tem em mãos),
    Conta XXXX (indica a conta onde recebe o salário por exemplo)
    """
    nome = models.CharField("Nome", max_length = 80)
    ehContaBancaria = models.BooleanField("É uma conta bancária")

    def get_absolute_url(self):
        return reverse('financas:conta_list')

    def __str__(self):
        return self.nome    

class CartaoCredito(models.Model):
    """
    Cadastro que visa facilitar o controle sobre despesas de cartão de crédito
    """
    nome = models.CharField("Descrição", max_length = 80)
    numero = models.CharField("Número do Cartão de Crédito", max_length = 80)
    observacao = models.TextField("Observação", default=" ", blank=True)
    dia_fechamento_fatura = models.IntegerField("Dia de fechamento da fatura", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('financas:cartaocredito_list')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cartão de Crédito'
        verbose_name_plural = 'Cartões de Crédito'
        ordering = ["numero"]

class Saque(models.Model):
    """
    Cadastro onde usuário vai poder registrar o que foi feito com valor sacado em algum momento. Exemplo:
    usuário saca 120 reais, sendo que 60 reais são para pagar uma conta X, 30 conta Y e mais 30 para ficar na carteira. 
    Cada um destes valores será um lançamento financeiro dentro do sistema.
    """
    descricao = models.CharField("Descrição", max_length = 50, default=" ")    
    conta = models.ForeignKey(Conta, null=True, blank=True)
    data_saque = models.DateTimeField("Data do saque")
    valor_saque = models.DecimalField("Valor saque", max_digits=19, decimal_places=10, default=0)
    
    #def getListaLancamentosFinanceiros(pk):
    #    return LancamentoFinanceiro.Objects.filter(saque.pk=pk)

    def get_absolute_url(self):
        return reverse('financas:saque_list')

    def __str__(self):
        return str(self.data_saque) + " - " + self.conta.nome

    def save(self, *args, **kwargs):
       # Se valor do saque for diferente do valor total de lançamentos vinculados ao saque, subir exceção 
       # totalLanctos = LancamentoFinanceiro.Objects.Agre     
        super(Saque, self).save(*args, **kwargs)


    def delete(self, using=None, keep_parents=False):
        lanctosPagos = LancamentoFinanceiro.Objects.filter(status = STATUS_CHOICES.Pago)
        if lanctosPagos is None:
            return super(Saque, self).delete(using, keep_parents)
        else:
            return django.http.HttpResponseBadRequest("Saque não pode ser apagado pois possui lançamentos financeiros pagos.") 

class LancamentoFinanceiro(models.Model):
    """
    Tabela base do sistema que representa os lançamentos financeiros que permitem ao usuário
    uma visão sobre como anda sua administração financeiras
    """
    TIPO_CHOICES = (('1', 'A Receber'), ('2', 'A Pagar'))
    STATUS_CHOICES = (('0', 'Não Pago'), ('1', 'Pago'))
    
    
    pessoa = models.ForeignKey(Pessoa, null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    data_emissao = models.DateField("Data emissão")
    classificacao = models.ForeignKey(Classificacao, null=True, blank=True)
    saque = models.ForeignKey(Saque, null=True, blank=True)
    cartaoCredito = models.ForeignKey(CartaoCredito, null=True, blank=True)
    conta = models.ForeignKey(Conta, null=True, blank=True)    
    valor = models.DecimalField("Valor", max_digits=19, decimal_places=10, default=0)
    data_pagto = models.DateField("Data pagamento", null=True, blank=True)
    descricao = models.CharField("Descrição", max_length = 50, default=" ", null=True, blank=True)
    status = models.CharField(max_length=1, choices = STATUS_CHOICES, default="0 ", null=True, blank=True) 

    def get_absolute_url(self):
        return reverse('financas:lancamentofinanceiro_list')

    def __str__(self):
        return str(self.pk) + " - " + str(self.valor)

    class Meta:
        verbose_name = 'Lançamento Financeiro'
        verbose_name_plural = 'Lançamentos Financeiros'
        ordering = ["pk"]
