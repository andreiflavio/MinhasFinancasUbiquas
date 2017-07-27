from django.contrib import admin
from .models import Classificacao, Conta, CartaoCredito, Saque, LancamentoFinanceiro

admin.site.register(Classificacao)
admin.site.register(Conta)
admin.site.register(CartaoCredito)
admin.site.register(Saque)
admin.site.register(LancamentoFinanceiro)
