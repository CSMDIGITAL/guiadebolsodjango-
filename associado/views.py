from django.shortcuts import render, redirect, get_object_or_404
from .models import Associado
from .forms import AssociadoForm

def dashboard(request):
    total = Associado.objects.count()
    ativos = Associado.objects.filter(status='Ativo').count()
    inativos = Associado.objects.exclude(status='Ativo').count()
    recentes = Associado.objects.order_by('-data_cadastro')[:6]

    contexto = {
        'total': total,
        'ativos': ativos,
        'inativos': inativos,
        'recentes': recentes,
    }

    return render(request, 'associado/dashboard.html', contexto)

def perfil(request):
    associado = {
        'id': '001',
        'nome': 'Cassio',
        'status': 'Ativo'
    }
    return render(request, 'associado/perfil.html', {'associado': associado})

def carteirinha(request):
    return render(request, 'associado/carteirinha.html')

def beneficio(request):
    return render(request, 'associado/beneficio.html')

def contato(request):
    return render(request, 'associado/contato.html')

def lista_associados(request):
    associados = Associado.objects.all().order_by('nome')
    return render(request, 'associado/lista.html', {'associados': associados})

def criar_associado(request):
    if request.method == 'POST':
        form = AssociadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_associados')
    else:
        form = AssociadoForm()
    return render(request, 'associado/form.html', {'form': form, 'titulo': 'Novo Associado'})

def editar_associado(request, id):
    associado = get_object_or_404(Associado, id=id)

    if request.method == 'POST':
        form = AssociadoForm(request.POST, request.FILES, instance=associado)
        if form.is_valid():
            form.save()
            return redirect('lista_associados')
    else:
        form = AssociadoForm(instance=associado)

    return render(request, 'associado/form.html', {'form': form, 'titulo': 'Editar Associado'})

def carteirinha_associado(request, id):
    associado = get_object_or_404(Associado, id=id)
    return render(request, 'associado/carteirinha_dinamica.html', {'associado': associado})

from django.shortcuts import get_object_or_404

def validar_associado(request, id):
    associado = get_object_or_404(Associado, id=id)
    return render(request, 'associado/validar.html', {'associado': associado})