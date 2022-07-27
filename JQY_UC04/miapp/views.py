from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
# Create your views here.
layout = """"""
def integrantes(request):
    integrantes = ['Julca Espillco Humberto','Quintana Quispe Alegria','Yauricasa mendoza Miguel']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Bienvenidos a la UNTELS',
        'mensaje':'Proyecto para la Unidad de Evaluativa N°4'
    })