from django.urls import path
from .views import home, contacto, galeria, agregar_producto, Listar_producto, Modificar_producto, Eliminar_producto

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('Listar-producto/', Listar_producto, name="Listar_producto"),
    path('Modificar-producto/<id>/', Modificar_producto, name="Modificar_producto"),
    path('Eliminar-producto/<id>/', Eliminar_producto, name="Eliminar_producto"),
]