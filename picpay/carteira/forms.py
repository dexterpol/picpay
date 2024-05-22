from django import forms

class AddSaldoForm(forms.Form):
    saldo = forms.DecimalField(max_digits=10, decimal_places=2, label='Adicionar Saldo')