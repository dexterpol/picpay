from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddSaldoForm
from .models import Carteira
from decimal import Decimal
from django.http import HttpResponse


    

@login_required(login_url='/login/')
def add_saldo(request):
    if request.user.is_superuser:  
        if request.method == 'POST':
            form = AddSaldoForm(request.POST)
            if form.is_valid():
                saldo = form.cleaned_data['saldo']
                carteir, created = Carteira.objects.get_or_create(usuario=request.user)
                carteir.saldo += Decimal(saldo)
                carteir.save()
                return redirect('transacao') 
        else:
            form = AddSaldoForm()

        context = {
            'form': form,
        }

        return render(request, 'add_saldo.html', context)
    else:
        return htt  # Redireciona para outra página se o usuário não for um superusuário
