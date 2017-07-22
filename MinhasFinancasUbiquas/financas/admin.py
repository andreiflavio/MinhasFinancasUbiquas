from django.contrib import admin
from .models import Classificacao, Conta, CartaoCredito

admin.site.register(Classificacao)
admin.site.register(Conta)
admin.site.register(CartaoCredito)
