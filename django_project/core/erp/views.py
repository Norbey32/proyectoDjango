from django.shortcuts import render
from core.erp.models import Category, Product


# Create your views here.

def MyfirstView(request):
    data = {
        'name': 'Norbey',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)

def MysecondView(request):
    data = {
        'name': 'Norbey',
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)