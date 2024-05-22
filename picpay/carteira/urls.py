from django.urls import path
from . import views

urlpatterns = [
    path('saldo/', views.add_saldo, name='saldo'),
]

