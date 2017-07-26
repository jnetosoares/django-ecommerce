from django.shortcuts import render

# Create your views here.

from .models import Product, Category

def product_list(request):
    context = {
        'produtos': Product.objects.all(),
    }
    return render(request,'catolog/produto_list.html',context)



# def categoria_por_id(request, pk):
#     categoria = Category.objects.get(id=pk)
#     context = {
#         'categoria_atual': categoria,
#         'produtos': Product.objects.filter(category=categoria),
#     }
#     return render(request,'catolog/produtos_por_categoria.html',context)

def categoria(request, slug):
    categoria = Category.objects.get(slug=slug)
    context = {
        'categoria_atual': categoria,
        'produtos': Product.objects.filter(category=categoria),
    }
    return render(request,'catolog/produtos_por_categoria.html',context)

def produto(request, slug):
    produto = Product.objects.get(slug=slug)
    context = {
        'produto': produto,
    }
    return render(request,'catolog/produto.html',context)
