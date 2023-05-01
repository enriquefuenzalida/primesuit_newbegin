from django.urls import path, include
from .views import home, contacto, galeria, agregar_producto, Listar_producto, Modificar_producto, Eliminar_producto, registro, ProductoViewset, MarcaViewset, galeriajson, marcasjson
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('galeriajson/', galeriajson, name="galeriajson"),
    path('marcasjson/', marcasjson, name="marcasjson"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('Listar-producto/', Listar_producto, name="Listar_producto"),
    path('Modificar-producto/<id>/', Modificar_producto, name="Modificar_producto"),
    path('Eliminar-producto/<id>/', Eliminar_producto, name="Eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
]