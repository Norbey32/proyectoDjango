from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def MyfirstView(request):
    data = {
        'name': 'Norbey'
    }
    return render(request, 'index.html', data)