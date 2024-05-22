
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm , CadastroForm , TransacaoForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from carteira.models import *
from .autorizador import validate_transaction
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print('entrando')
                form_trasacao= TransacaoForm()
                form_trasacao.remetente = request.user
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




@login_required(login_url='/login/')
def transacao(request):
    saldo_carteira = request.user.carteira.saldo
    if request.method == 'POST':
        
        form = TransacaoForm(request.POST)
        mock_response_url = "https://picpay.free.mockoapp.net/transacao"  
        is_transaction_authorized = validate_transaction(mock_response_url)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            destinatario = form.cleaned_data['destinatario']
            transacao = form.save(commit=False)
            transacao.remetente = request.user 
            if is_transaction_authorized:
                if request.user.carteira.saldo >= transacao.valor:
                    request.user.carteira.saldo -= valor
                    request.user.carteira.save()
                    destinatario.carteira.saldo += valor
                    destinatario.carteira.save()
                    transacao.save()
                    print('saldo enviado para')
                    return redirect('dashboard')
                else:
                    return render(request, 'dashboard.html', {'form': form, 'error_message': 'Saldo insuficiente.'})
            else:
                return render(request, 'dashboard.html', {'form': form, 'error_message': 'Saldo insuficiente.'})
    else:            
        saldo_carteira = request.user.carteira.saldo
        form = TransacaoForm()

    return render(request, 'dashboard.html', {'form': form , 'saldo_carteira':saldo_carteira})


@login_required(login_url="/login/")
def dashboard(request):
    print('oi')
    return render(request, 'dashboard.html')


def cadastro (request):
    if request.method  == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            print('cadastro concluido')
            return HttpResponse('cadastro concluido') 
    else:
        form = CadastroForm()
    return render(request , 'cadastro.html' , {'form':form})