from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Transacao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    remetente = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='transacoes_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='transacoes_recebidas', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    carteira = models.OneToOneField('carteira.Carteira', on_delete=models.CASCADE, null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups', 
        blank=True,
        help_text='The groups this user belongs to. A user can belong to multiple groups.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions', 
        blank=True,
        help_text='Specific permissions for this user.'
    )
