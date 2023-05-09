from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST']) 
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']

    try:
        user = User.objects.get(username=username)#select * from users where username=username;
    except User.DoesNotExist:
        return Response("Usuario incorrecto")
    
    #validamos la pass

    pass_valido =  check_password(password, user.password)
    if not pass_valido: #pass_valido = True
        return Response("Clave incorrecta")
    
    #permite crear o recuperar el token
    token, created =  Token.objects.get_or_create(user=user) #select key from token user=users:
    return Response(token.key)