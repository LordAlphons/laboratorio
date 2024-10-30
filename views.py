from django.shortcuts import render, redirect
from .models import Laboratorio

def index(request):
    laboratorios = Laboratorio.objects.all().order_by('id')
    context = {
        'laboratorios': laboratorios,
    }
    return render(request, 'index.html', context)

# Insertar Laboratorio
def insertar_lab(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        return redirect('index')
    else:
        return render(request, 'insertar.html')

# Editar Laboratorio
def editar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    
    context = {
        'laboratorio': laboratorio,
    }

    return render(request, 'editar.html', context)

# Actualizar Laboratorio
def actualizar_laboratorio(request, id):
    nombre = request.POST['nombre']
    ciudad = request.POST['ciudad']
    pais = request.POST['pais']
    laboratorio = Laboratorio.objects.get(id=id)
    laboratorio.nombre = nombre
    laboratorio.ciudad = ciudad
    laboratorio.pais = pais
    laboratorio.save()
    return redirect('index')

# Eliminar Laboratorio
def eliminar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('index')
    
    context = {
        'laboratorio': laboratorio,
    }
    return render(request, 'eliminar.html', context)