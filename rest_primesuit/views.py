from django.shortcuts import render
from rest_framework import status
from django.core.paginator import Paginator
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Producto, Marca
from .serializers import ProductoSerializer, MarcaSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def Listar_producto(request):
    if request.method == 'GET':
        SET = Producto.objects.all()
        serializer_class = ProductoSerializer(SET, many=True)
        return Response(serializer_class.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_class =  ProductoSerializer(data = data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.error, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_producto_mod(request, id):
    try:
        p = Producto.objects.get(id = id) #select * from mascota where codigoChip = id
    except Producto.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(p)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(p, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
           return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        p.delete()
        return Response(status= status.HTTP_204_NO_CONTENT) 

