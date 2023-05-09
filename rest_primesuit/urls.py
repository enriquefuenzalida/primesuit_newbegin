from django.urls import path, include
from .views import Listar_producto , vista_producto_mod
from rest_primesuit.viewLogin import login



urlpatterns = [
    path('Listar', Listar_producto, name="Listar"),
    path('datos/<id>', vista_producto_mod, name="datos"),
    path('login-sesion/', login, name="login-sesion"),
]