from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Saque

class SaqueForm(forms.ModelForm):
    """Form definition for Saque."""

    class Meta:
        """Meta definition for Saqueform."""

        model = Saque
        fields = ['descricao' ,'conta', 'data_saque', 'valor_saque']

        error_messages = {
            'descricao': {
                'max_length': _("Descrição pode conter até 80 caracteres."),
            },
        }
