from lista.models import Produtos
from lista.serializer import ListaSerializer

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json

from . import funcoes as fn


@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = Produtos.objects.all()                          # Get all objects in User's database (It returns a queryset)

        serializer = ListaSerializer(users, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT'])
def get_by_nick(request, id):

    try:
        user = Produtos.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ListaSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':

        serializer = ListaSerializer(Produtos, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)




#Endpoints para o CRUD

@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):

# ACESSOS

    if request.method == 'GET':

        users = Produtos.objects.all()                          # Get all objects in User's database (It returns a queryset)

        serializer = ListaSerializer(users, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_user = request.data
        
        serializer = ListaSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        id = request.data['id']

        try:
            updated_product = Produtos.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ListaSerializer(updated_product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)



# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            user_to_delete = Produtos.objects.get(pk=request.data['user_nickname'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
