from django.db import models
from django.conf import settings

class Carteira(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Carteira de {self.usuario.username} com saldo {self.saldo}"





