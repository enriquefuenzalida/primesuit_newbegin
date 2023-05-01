from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForms, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

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

@permission_required('app.add_producto')
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

@permission_required('app.view_producto')
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

@permission_required('app.change_producto')
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

@permission_required('app.delete_producto')
def Eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamentem")
    return redirect(to="Listar_producto")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Has sido registrado")
            return redirect(to="home")
        data["form"] = formulario
    return render(request,'registration/registro.html', data)
