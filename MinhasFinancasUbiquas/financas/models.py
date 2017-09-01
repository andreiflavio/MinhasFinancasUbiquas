from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.core.urlresolvers import reverse
from MinhasFinancasUbiquas.core.models import Pessoa
from .rules import *
from .choices import *

# Documentação base para implementação deste model: https://docs.djangoproject.com/en/1.11/topics/db/models/
class Classificacao(models.Model):
    """
    Neste cadastro serão definidos como usuário deseja classificar seus lançamentos financeiros. Exemplo: 
    Gastos Férias, Namoro, Passeios, Gastos Essenciais, Gastos Supérfluos, entre outras categorias que 
    o usuário deseja.
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
    dia_vencimento_fatura = models.IntegerField("Dia de pagamento da fatura", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('financas:cartaocredito_list')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cartão de Crédito'
        verbose_name_plural = 'Cartões de Crédito'
        ordering = ["numero"]

class LancamentoFinanceiro(models.Model):
    """
    Tabela base do sistema que representa os lançamentos financeiros que permitem ao usuário
    uma visão sobre como anda sua administração financeiras
    """            
    descricao = models.CharField("Descrição", max_length = 50, default=" ", null=True, blank=True)
    data = models.DateField("Data")
    valor = models.DecimalField("Valor", max_digits=19, decimal_places=10, default=0)
    status = models.IntegerField("Status", choices = STATUS_CHOICES, default="1", null=False, blank=True) 
    tipo = models.IntegerField("Tipo", choices=TIPO_CHOICES, null=False, blank=True)    
    classificacao = models.ForeignKey(Classificacao, null=True, blank=True)
    conta = models.ForeignKey(Conta, null=True, blank=True) 
    cartaoCredito = models.ForeignKey(CartaoCredito, null=True, blank=True)
    observacao = models.TextField("Informações adicionais", null=True, blank=True)
                    

    def get_absolute_url(self):
        return reverse('financas:lancamentofinanceiro_list')

    def __str__(self):
        return str(self.pk) + "." + self.descricao + " - " + str(self.valor)

    def getLanctos(valueSearch):
        ##https://medium.com/@csantosmachado/compondo-querysets-no-django-utilizando-objetos-q-c88bc3f65031
        if valueSearch is not None:
            lanctos = LancamentoFinanceiro.objects.filter(Q(descricao__icontains=valueSearch))
        else:
            lanctos = LancamentoFinanceiro.objects.all()
        return lanctos
        

    class Meta:
        verbose_name = 'Lançamento Financeiro'
        verbose_name_plural = 'Lançamentos Financeiros'
        ordering = ["pk"]
