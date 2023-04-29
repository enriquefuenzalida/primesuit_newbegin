from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm, ProductoForms

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
             data["form"] = formulario
    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):

    data = {
        'form' : ProductoForms()
    }

    if request.method == "POST":
        formulario = ProductoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto guardado"
        else:
             data["form"] = formulario

    return render(request,'app/producto/agregar.html', data)

def Listar_producto(request):

    productos = Producto.objects.all()

    data = {
        'productos' : productos
    }

    return render(request,'app/producto/listar.html', data)
