from django.db import models
from django.core.urlresolvers import reverse
from core.models import Pessoa

# Documentação base para implementação deste model: https://docs.djangoproject.com/en/1.11/topics/db/models/
class Classificacao(models.Model):
    """
    Neste cadastro serão definidos como usuário deseja classificar seus lançamentos financeiros. Exemplo: 
    Gastos Férias, Namoro, Passeios, Gastos Essenciais, Gastos Supérfluos, entre outras categorias que o usuário deseja.
    """
    nome = models.CharField("Nome", max_length = 80)

    def get_absolute_url(self):
        return reverse('financas:classificacao_list')

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

class CartaoCredito(models.Model):
    """
    Cadastro que visa facilitar o controle sobre despesas de cartão de crédito
    """
    nome = models.CharField("Descrição", max_length = 80)
    numero = models.CharField("Número do Cartão de Crédito", max_length = 80)
    observacao = models.TextField("Observação", default=" ", blank=True)

    def get_absolute_url(self):
        return reverse('financas:cartaocredito_list')

class Saque(models.Model):
    """
    Cadastro onde usuário vai poder registrar o que foi feito com valor sacado em algum momento. Exemplo:
    usuário saca 120 reais, sendo que 60 reais são para pagar uma conta X, 30 conta Y e mais 30 para ficar na carteira. 
    Cada um destes valores será um lançamento financeiro dentro do sistema.
    """
    descricao = models.CharField("Descrição", max_length = 50)    
    conta = models.ForeignKey(Conta, null=True, blank=True)
    data_saque = models.DateTimeField("Data do saque")
    
    def getListaLancamentosFinanceiros(self):
        return LancamentoFinanceiro.Objects.filter(self.pk = saque.pk)

    def get_absolute_url(self):
        return reverse('financas:saques_list')

class LancamentoFinanceiro(models.Model):
    """
    Tabela base do sistema que representa os lançamentos financeiros que permitem ao usuário
    uma visão sobre como anda sua administração financeiras
    """
    TIPO_CHOICES = (('1', 'A Receber'), ('2', 'A Pagar'))

    pessoa = models.ForeignKey(Pessoa, null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    data_emissao = models.DateField("Data emissão")
    classificacao = models.ForeignKey(Classificacao, null=True, blank=True)
    saque = models.ForeignKey(Saque, null=True, blank=True)
    cartaoCredito = models.ForeignKey(CartaoCredito, null=True, blank=True)
    conta = models.ForeignKey(Conta, null=True, blank=True)    

    data_pagto = models.DateField("Data pagamento", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('financas:lancamentofinanceiro_list')
