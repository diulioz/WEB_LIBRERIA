from django.shortcuts import render
from django.http import HttpResponse
from .models import libro
from .forms import LibroForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib import messages

# Create your views here.

# @login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def empezar(request):
    return render(request, 'libros/index.html')

@login_required
def libros(request):
    libros = libro.objects.all() 
    return render(request, 'libros/index.html' , {'Libros':libros})

def crear(request):
    formulario =LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html' , {'formulario': formulario})

def editar(request, id):
    libro1 = libro.objects.get(id=id)
    formulario =LibroForm(request.POST or None, request.FILES or None, instance=libro1)
    if formulario.is_valid and request.POST:
        formulario.save()
    return render(request, 'libros/editar.html',{'formulario':formulario})

def borrar(request, id):
    libro1 = libro.objects.get(id=id)
    libro1.delete()
    return redirect('libros')

def salir(request):
    logout(request)
    messages.info(request,f"Tu sesión se ha cerrado correctamente")
    # messages.success(request, f"Sesión terminada")
    # return redirect('/')
    return render(request, 'paginas/inicio.html')

