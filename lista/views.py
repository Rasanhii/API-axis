from lista.models import Produtos
from lista.serializer import ListaSerializer


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = Produtos.objects.all()                          # Get all objects in User's database (It returns a queryset)

        serializer = ListaSerializer(users, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT'])
def get_by_nick(request, nick):

    try:
        user = Produtos.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ListaSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':

        serializer = ListaSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)




# CRUDZAO DA MASSA
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['user']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                user_nickname = request.GET['user']         # Find get parameter

                try:
                    user = Produtos.objects.get(pk=user_nickname)   # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = ListaSerializer(user)           # Serialize the object data into json
                return Response(serializer.data)            # Return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

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

        nickname = request.data['user_nickname']

        try:
            updated_user = Produtos.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
        print('Resultado final ', fn.soma(1,2))

        serializer = ListaSerializer(updated_user, data=request.data)

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




