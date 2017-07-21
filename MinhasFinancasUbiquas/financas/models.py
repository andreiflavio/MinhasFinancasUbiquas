from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Classificacao(models.Model):
    nome = models.CharField(max_length = 80)

    def get_absolute_url(self):
        return reverse('financas:classificacao_list')