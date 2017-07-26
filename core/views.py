# coding=utf-8
from django.shortcuts import render

from django.http import HttpResponse

from catolog.models import Category, Product
# Create your views here.

def index(request):
    #texto = ['Projeto Supervisionado', 'Django e-commerce', 'IFPI']
    return render(request, 'index.html')

# def produto(request):
#     return render(request, 'produto.html')

# def produto_list(request):
#     return render(request, 'produto_list.html')

def contato(request):
    return render(request, 'contato.html')

