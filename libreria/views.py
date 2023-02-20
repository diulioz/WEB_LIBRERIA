from django.shortcuts import render
from django.http import HttpResponse
from .models import libro
from .forms import LibroForm
from django.shortcuts import redirect

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = libro.objects.all() 
    return render(request, 'libros/index.html' , {'Libros':libros})
def crear(request):
    formulario =LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html' , {'formulario': formulario})
def editar(request):
    return render(request, 'libros/editar.html')

def eliminar(request,idd):
    libro.objects.get(idd=idd).delete()
    # return redirect('/index.html')
    return render(request, 'libros/index.html')

# def actualizar(request):
#     idd = request.POST['idd']
#     titulo = request.POST['titulo']
#    # imagen = request.FILES['imagen']
#     descripcion = request.POST['descripcion']
#     Libro.objects.filter(idd=idd).update(titulo=titulo,descripcion=descripcion)
    
#     return redirect('/index.html')