from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForms
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

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
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'app/galeria.html', data)

def agregar_producto(request):

    data = {
        'form' : ProductoForms()
    }

    if request.method == "POST":
        formulario = ProductoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto guardado")
        else:
             data["form"] = formulario

    return render(request,'app/producto/agregar.html', data)

def Listar_producto(request):

    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 2)
        productos = paginator. page(page)
    except:
        raise Http404


    data = {
        'entity' : productos,
        'paginator' : paginator
    }

    return render(request,'app/producto/listar.html', data)

def Modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    data = {
        'form':ProductoForms(instance=producto)
    }
    if request.method == "POST":
        formulario = ProductoForms(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamentem")
            return redirect(to="Listar_producto")
        data["form"] = formulario
             

    return render(request,'app/producto/modificar.html',data)

def Eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamentem")
    return redirect(to="Listar_producto")