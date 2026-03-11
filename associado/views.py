from django.shortcuts import render

def index(request):
    return render(request, 'associado/index.html')

def perfil(request):
    return render(request, 'associado/perfil.html')

def carteirinha(request):
    return render(request, 'associado/carteirinha.html')

def beneficio(request):
    return render(request, 'associado/beneficio.html')

def contato(request):
    return render(request, 'associado/contato.html')
