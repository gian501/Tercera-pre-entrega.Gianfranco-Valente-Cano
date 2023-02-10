from django.shortcuts import render
from django.http import HttpResponse
from App03.models import Curso

# Create your views here.

def inicio(request):
    return render(request, 'App03/inicio.html') # usar el nombre del template
    #return HttpResponse('Vista Inicio')

def cursos(request):
    return render(request, 'App03/cursos.html')
    #return HttpResponse('Vista cursos')

def profesores(request):
    return render(request, 'App03/profesores.html')
    #return HttpResponse('Vista profesores')

def entregables(request):
    return render(request, 'App03/entregables.html')
    #return HttpResponse('Vista entregables')

def estudiantes(request):
    return render(request, 'App03/estudiantes.html')
    #return HttpResponse('Vista estudiantes')