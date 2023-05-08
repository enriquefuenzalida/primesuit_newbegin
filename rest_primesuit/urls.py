from django.urls import path, include
from .views import Listar_producto



urlpatterns = [
    path('Listar', Listar_producto, name="Listar"),
]