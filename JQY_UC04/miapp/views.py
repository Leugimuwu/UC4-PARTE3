from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from miapp.models import Estudiante
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
# creamos estudiantes
def crear_estudiante(request):
    estudiante=Estudiante(
    codigo = "137258369",
    dni = "69788869",
    nombre="Humberto",
    apepat="Julca",
    apemat="Espillco",
    direccion="Jiron de la Union",
    telefono="955525874",
    estado="A"
    )
    estudiante.save()
    return HttpResponse (f"<h1>Estudiante registrado:</h1> "+
    f"<br> <b>Código:</b> {estudiante.codigo} <br> <b>DNI:</b> {estudiante.dni} <br> <b>Nombre:</b> {estudiante.nombre} <br> "+
    f"<b>Apellido paterno:</b> {estudiante.apepat} <br> <b>Apellido materno:</b> {estudiante.apemat} <br><b>Dirección:</b> "+
    f" {estudiante.direccion} <br> <b>Telefono:</b> {estudiante.telefono} <br> <b>Estado:</b> {estudiante.estado}")
    
