from django.contrib import admin
from .models import  *
from carteira.models import *
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']

admin.site.register(Transacao)
admin.site.register(Carteira)
