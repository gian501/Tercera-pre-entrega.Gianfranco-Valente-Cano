from django.shortcuts import render
from django.http import HttpResponse
from App03.models import Curso
from App03.forms import CursoFormulario

# Create your views here.

def inicio(request):
    return render(request, 'App03/inicio.html') # usar el nombre del template
    #return HttpResponse('Vista Inicio')

def cursos(request):
    if request.method == "POST":
 
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "App03/cursos.html", )
    else:
        miFormulario = CursoFormulario()
    return render(request, 'App03/cursos.html',{"miFormulario": miFormulario})
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