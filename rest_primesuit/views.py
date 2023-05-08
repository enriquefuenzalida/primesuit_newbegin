from django.shortcuts import render
from rest_framework import status
from django.core.paginator import Paginator
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Producto, Marca
from .serializers import ProductoSerializer, MarcaSerializers

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
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




