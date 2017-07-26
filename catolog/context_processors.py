from .models import Category

def categorias(request):
    return {
        'categorias': Category.objects.all(),
    }