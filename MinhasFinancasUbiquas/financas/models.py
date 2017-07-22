from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Classificacao(models.Model):
    nome = models.CharField("Nome", max_length = 80)

    def get_absolute_url(self):
        return reverse('financas:classificacao_list')

class Conta(models.Model):
    nome = models.CharField("Nome", max_length = 80)
    ehContaBancaria = models.BooleanField("É uma conta bancária")

    def get_absolute_url(self):
        return reverse('financas:conta_list')

class CartaoCredito(models.Model):
    nome = models.CharField("Descrição", max_length = 80)
    numero = models.CharField("Número do Cartão de Crédito", max_length = 80)
    observacao = models.TextField("Observação", default=" ", blank=True)

    def get_absolute_url(self):
        return reverse('financas:cartaocredito_list')