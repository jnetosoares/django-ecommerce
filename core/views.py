# coding=utf-8
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    texts = ['Exemplo', 'Django e-commerce', 'Udemy']
    context = {
        'title': 'django e-commerce',
        'texts': texts
    }
    return render(request, 'index.html', context)

def produto(request):
    return render(request, 'produto.html')

def produto_list(request):
    return render(request, 'produto_list.html')

def contato(request):
    return render(request, 'contato.html')

