from django.shortcuts import render

def category_list(request):
    data = {
        'title': 'Listado de Categorias'
    }
    return render(request, 'category/list.html', data)