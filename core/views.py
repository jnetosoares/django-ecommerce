# coding=utf-8
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    texto = ['Projeto Supervisionado', 'Django e-commerce', 'IFPI']
    context = {
        'title': 'django e-commerce',
        'texto': texto
    }
    return render(request, 'index.html', context)

def produto(request):
    return render(request, 'produto.html')

def produto_list(request):
    return render(request, 'produto_list.html')

def contato(request):
    return render(request, 'contato.html')

